from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.orders_model import Order
from app.models.books_model import Book

def create_order(user_id: int, book_id: int, db: Session):
    book = db.query(Book).filter(Book.id == book_id, Book.is_deleted == False).first()
    if not book:
        raise HTTPException(status_code=400, detail="Book not available")
    order = Order(user_id=user_id, book_id=book_id)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_orders(user_id: int, db: Session):
    return db.query(Order).filter(Order.user_id == user_id).all()