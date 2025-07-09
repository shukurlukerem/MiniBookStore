from sqlalchemy import Column, Integer, String, Boolean
from app.core.config import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    description = Column(String)
    is_deleted = Column(Boolean, default=False) # true olduqda gorunmeyecek