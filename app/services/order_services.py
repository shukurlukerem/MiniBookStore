from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from app.models.orders_model import Order
from app.models.books_model import Book
from app.core.security import oauth2_scheme, verify_token

def create_order(user_id: int, book_id: int, db: Session, token: str = Depends(oauth2_scheme)):
    try:
        username = verify_token(token)
        book = db.query(Book).filter(Book.id == book_id, Book.is_deleted == False).first()
        if not book:
            raise HTTPException(status_code=400, detail="Book not available")
        
        order = Order(user_id=user_id, book_id=book_id)
        db.add(order)
        db.commit()
        db.refresh(order)
        return order

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")

def get_orders(user_id: int, db: Session, token: str = Depends(oauth2_scheme)):
    try:
        username = verify_token(token)
        orders = db.query(Order).filter(Order.user_id == user_id).all()
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")
