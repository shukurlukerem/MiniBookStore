from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.schema.book_schema import BookCreate
from app.services.book_services import (
    create_book,
    get_books,
    get_book,
    update_book,
    delete_book
)
from app.core.config import get_db
from app.core.security import oauth2_scheme

router = APIRouter()


@router.get("/get-all-books")
def route_get_books(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_books(db, token)


@router.post("/add-new-book")
def route_add_book(book: BookCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return create_book(book, db, token)


@router.get("/get-one-book/{book_id}")
def route_get_book(book_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_book(book_id, db, token)


@router.put("/update-book/{book_id}")
def route_update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return update_book(book_id, book, db, token)


@router.delete("/delete-book/{book_id}")
def route_delete_book(book_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return delete_book(book_id, db, token)
