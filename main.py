from fastapi import FastAPI
from app.api.v1.routes import auth_routes, book_routes, orders_routes
from app.core.config import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini BookStore")

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(book_routes.router, prefix="/books", tags=["Books"])
app.include_router(orders_routes.router, prefix="/orders", tags=["Orders"])


@app.get("/test")
def test():
    return {"message": "Mini Bookstore API is running!"}