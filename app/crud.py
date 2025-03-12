from sqlalchemy.orm import Session
from . import models, schemas

def get_bookmark(db: Session, bookmark_id: int):
    return db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()

def get_bookmarks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Bookmark).offset(skip).limit(limit).all()

def create_bookmark(db: Session, bookmark: dict):
    db_bookmark = models.Bookmark(**bookmark)
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark

def get_bookmark_count(db: Session):
    return db.query(models.Bookmark).count()

def get_total_clicks(db: Session):
    result = db.query(models.Bookmark).with_entities(models.Bookmark.clicks).all()
    return sum(click[0] for click in result)

def get_popular_bookmarks(db: Session, limit: int = 5):
    bookmarks = db.query(models.Bookmark).order_by(models.Bookmark.clicks.desc()).limit(limit).all()
    return [{"id": b.id, "url": b.url, "title": b.title, "clicks": b.clicks} for b in bookmarks]
