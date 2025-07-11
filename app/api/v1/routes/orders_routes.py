from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.schema.order_schema import OrderCreate
from app.services.order_services import create_order, get_orders
from app.core.config import get_db
from fastapi.security import OAuth2PasswordBearer
from fastapi_limiter.depends import RateLimiter

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter()

@router.post("/make-order", dependencies=[Depends(RateLimiter(times=100, seconds=600))])
def make_order(order: OrderCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return create_order(book_id=order.book_id, db=db, token=token)

@router.get("/order-list", dependencies=[Depends(RateLimiter(times=100, seconds=600))])
async def list_orders(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    orders = await get_orders(db=db, token=token)
    return orders

