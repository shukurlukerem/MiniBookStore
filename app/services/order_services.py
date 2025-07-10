from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from app.models.orders_model import Order
from app.models.books_model import Book
from app.core.security import verify_token

def create_order(book_id: int, db: Session, token: str):
    try:
        username = verify_token(token)  
        user_id = get_user_id_by_username(db, username)  
        
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


def get_orders(db: Session, token: str):
    try:
        username = verify_token(token)
        user_id = get_user_id_by_username(db, username)  
        orders = db.query(Order).filter(Order.user_id == user_id).all()
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")

def get_user_id_by_username(db: Session, username: str):
    from app.models.auth_model import User
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.id
