from pydantic import BaseModel

class OrderCreate(BaseModel):
    book_id: int