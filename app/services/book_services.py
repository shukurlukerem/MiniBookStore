from sqlalchemy.orm import Session
from app.models.books_model import Book

def create_book(book, db: Session):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(Book).filter(Book.is_deleted == False).all()

def get_book(book_id: int, db: Session):
    return db.query(Book).filter(Book.id == book_id, Book.is_deleted == False).first()

def update_book(book_id: int, book, db: Session):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book

def delete_book(book_id: int, db: Session):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db_book.is_deleted = True
        db.commit()