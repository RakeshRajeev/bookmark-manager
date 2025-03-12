from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class BookmarkBase(BaseModel):
    url: str
    title: Optional[str] = None

class BookmarkCreate(BookmarkBase):
    pass

class Bookmark(BookmarkBase):
    id: int
    slug: str
    clicks: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    bookmarks: list[Bookmark] = []

    class Config:
        orm_mode = True
