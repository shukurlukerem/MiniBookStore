FastAPI Bookstore & Orders API


Features

User registration and login with JWT authentication
CRUD operations on books (including soft delete)
Creating and listing user orders
Secure password hashing with Passlib


API Endpoints

Endpoint               Method Description                         
---------------------- ------ ----------------------------------- 
`/auth/register`       POST   Register a new user                 
`/auth/login`          POST   Login and get access token (JWT)    
`/books/add-new-book`  POST   Create a new book                   
`/books/get-all-books` GET    List all active books               
`/books/update-book`   PUT    Update book details                 
`/books/delete-book`   DELETE Soft delete a book                  
`/orders/make-order`   POST   Create a new order                  
`/orders/order-list`   GET    Get list of orders for current user 

---


Prerequisites

* Python 3.11
* PostgreSQL installed and running
* (Optional) Virtual environment tool (venv, pipenv, etc.)



 Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate   


Install dependencies

pip install -r requirements.txt
```

Setup

Configure your PostgreSQL database
pdate the database URL in your settings/config file
un migrations if you use Alembic or other tools


---

Tools & Libraries

FastAPI
PostgreSQL
SQLAlchemy
Python-Jose (JWT)
Passlib (Password hashing)
Uvicorn (ASGI server)

---

Usage

Use Postman or `curl` to test API endpoints
Authenticate with `/auth/login` to get JWT token
Add JWT token as Bearer token in the `Authorization` header to access protected routes


How to run
uvicorn app.main:app --reload
