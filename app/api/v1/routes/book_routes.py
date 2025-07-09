from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.schema.book_schema import BookCreate
from app.services.book_services import create_book, get_books, get_book, update_book, delete_book
from app.core.config import get_db

router = APIRouter()

@router.get("/get-all-books")
def list_books(db: Session = Depends(get_db)):
    return get_books(db)

@router.post("/add-new-book")
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(book, db)

@router.get("/get-one-book/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    return get_book(book_id, db)

@router.put("/update-book/{book_id}")
def edit_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    return update_book(book_id, book, db)

@router.delete("/delete-books/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    delete_book(book_id, db)
    return {"message": "Book soft-deleted"}