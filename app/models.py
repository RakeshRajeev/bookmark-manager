from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Booleanfrom sqlalchemy.orm import relationshipfrom database import Baseimport datetimeclass User(Base):    __tablename__ = 'users'    id = Column(Integer, primary_key=True)    email = Column(String(120), unique=True, nullable=False)    password = Column(String(255), nullable=False)    is_active = Column(Boolean, default=True)
    bookmarks = relationship("Bookmark", back_populates="user")

class Bookmark(Base):
    __tablename__ = 'bookmarks'
    id = Column(Integer, primary_key=True)
    url = Column(String(500), nullable=False)
    title = Column(String(200))
    slug = Column(String(200), unique=True, nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    clicks = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="bookmarks")
    description = Column(String(500))
    is_private = Column(Boolean, default=False)