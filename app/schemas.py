from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class BookmarkBase(BaseModel):
    url: HttpUrl
    title: Optional[str] = None
    description: Optional[str] = None
    is_private: bool = False

class BookmarkCreate(BookmarkBase):
    pass

class Bookmark(BookmarkBase):
    id: int
    slug: str
    created: datetime
    clicks: int
    user_id: Optional[int]

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
