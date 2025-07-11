from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.schema.order_schema import OrderCreate
from app.services.order_services import create_order, get_orders
from app.core.config import get_db
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter()

@router.post("/make-order")
def make_order(order: OrderCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return create_order(book_id=order.book_id, db=db, token=token)

@router.get("/order-list")
async def list_orders(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    orders = await get_orders(db=db, token=token)
    return orders

