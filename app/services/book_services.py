from sqlalchemy.orm import Session
from app.models.books_model import Book
from fastapi import HTTPException, status

def create_book(book, db: Session):
    try:
        db_book = Book(**book.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the book: {str(e)}")


def get_books(db: Session):
    try:
        return db.query(Book).filter(Book.is_deleted == False).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while purchasing the book.")


def get_book(book_id: int, db: Session):
    try:
        db_book = db.query(Book).filter(Book.id == book_id, Book.is_deleted == False).first()
        if not db_book:
            raise HTTPException(status_code=404, detail="ID not found")
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Error.")


def update_book(book_id: int, book, db: Session):
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if not db_book:
            raise HTTPException(status_code=404, detail="ID not found")
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")


def delete_book(book_id: int, db: Session):
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if not db_book:
            raise HTTPException(status_code=404, detail="ID not found")
        db_book.is_deleted = True
        db.commit()
        return {"message": "Book successfully deleted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Error.")
