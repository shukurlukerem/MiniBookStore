from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.books_model import Book
from app.core.security import verify_token
from fastapi_cache.decorator import cache
import asyncio


def create_book(book, db: Session, token: str):
    username = verify_token(token)
    try:
        db_book = Book(**book.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating book: {str(e)}")

@cache(expire=60)
async def get_books_cached(db: Session, token: str):
    try:
        username = verify_token(token)
        books = await asyncio.to_thread(lambda: db.query(Book).filter(Book.is_deleted == False).all())
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")


def get_book(book_id: int, db: Session, token: str):
    username = verify_token(token)
    try:
        db_book = db.query(Book).filter(Book.id == book_id, Book.is_deleted == False).first()
        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found")
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching book")


def update_book(book_id: int, book, db: Session, token: str):
    username = verify_token(token)
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if not db_book or db_book.is_deleted:
            raise HTTPException(status_code=404, detail="Book not found")
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating book: {str(e)}")


def delete_book(book_id: int, db: Session, token: str):
    username = verify_token(token)
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if not db_book or db_book.is_deleted:
            raise HTTPException(status_code=404, detail="Book not found")
        db_book.is_deleted = True
        db.commit()
        return {"message": "Book soft-deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error deleting book")
