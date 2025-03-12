from fastapi import FastAPI, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, get_db
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as redis
import hashlib
import string
import random
import datetime
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookmark Manager API")

@app.get("/")
async def root():
    return {"message": "Welcome to Bookmark Manager API"}

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate limiting setup
@app.on_event("startup")
async def startup():
    redis_instance = redis.from_url(
        settings.REDIS_URL, 
        encoding="utf-8", 
        decode_responses=True
    )
    await FastAPILimiter.init(redis_instance)

# URL shortening function
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.post("/bookmarks/", response_model=schemas.Bookmark)
def create_bookmark(bookmark: schemas.BookmarkCreate, db: Session = Depends(get_db)):
    return crud.create_bookmark(db=db, bookmark=bookmark)

@app.get("/bookmarks/", response_model=List[schemas.Bookmark])
def read_bookmarks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookmarks = crud.get_bookmarks(db, skip=skip, limit=limit)
    return bookmarks

@app.get("/bookmarks/{bookmark_id}", response_model=schemas.Bookmark)
def read_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    bookmark = crud.get_bookmark(db, bookmark_id=bookmark_id)
    if bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmark

@app.post("/shorten/", response_model=schemas.Bookmark)
async def create_short_url(
    response: Response,  # Add response parameter
    bookmark: schemas.BookmarkCreate, 
    request: Request,
    db: Session = Depends(get_db),
    _: bool = Depends(RateLimiter(times=10, seconds=60))  # Changed rate limiter usage
):
    bookmark_dict = bookmark.dict()
    bookmark_dict["slug"] = generate_short_url()
    return crud.create_bookmark(db=db, bookmark=bookmark_dict)

@app.get("/analytics/")
async def get_analytics(db: Session = Depends(get_db)):
    analytics = {
        "total_bookmarks": crud.get_bookmark_count(db),
        "total_clicks": crud.get_total_clicks(db),
        "popular_links": crud.get_popular_bookmarks(db, limit=5)
    }
    return analytics

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": datetime.datetime.utcnow()
    }
