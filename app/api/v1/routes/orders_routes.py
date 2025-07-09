from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.schema.order_schema import OrderCreate
from app.services.order_services import create_order, get_orders
from app.core.config import get_db
from app.core.config import get_db
from app.core.security import get_current_user
from app.models.auth_model import User


router = APIRouter()


@router.post("/make-order")
def make_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_order(user_id=current_user.id, book_id=order.book_id, db=db)

@router.get("/order-list")
def list_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_orders(user_id=current_user.id, db=db)