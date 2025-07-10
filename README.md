FastAPI Bookstore & Orders API
A simple REST API built with FastAPI, PostgreSQL, SQLAlchemy, and JWT for user authentication and managing books and orders.

Features
User registration and login with JWT authentication

CRUD operations on books (with soft delete)

Creating and listing user orders

Secure password hashing with Passlib

API Endpoints
Endpoint	Method	Description
/auth/register	POST	Register a new user
/auth/login	POST	Login and get access token (JWT)
/books/add-new-book	POST	Create a new book
/books/get-all-books	GET	Get list of all active books
/books/update-book	PUT	Update existing book details
/books/delete-book	DELETE	Soft delete a book
/orders/make-order	POST	Create a new order
/orders/order-list	GET	Get list of orders for current user

Getting Started
Prerequisites
Python 3.11

PostgreSQL installed and running

(Optional) Virtual environment tool (venv, pipenv, etc.)

Installation
Clone the repository

bash
Copy
Edit
git clone <repository-url>
cd <repository-folder>
Create and activate a virtual environment (recommended)

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up your PostgreSQL database and update the database URL in your settings/config file.

Run database migrations (if using Alembic or any ORM migrations tool)

Run the app

bash
Copy
Edit
uvicorn main:app --reload
Tools & Libraries Used
FastAPI

PostgreSQL

SQLAlchemy

Python-Jose (JWT)

Passlib (Password hashing)

Uvicorn (ASGI server)

Usage
Use Postman or curl to interact with API endpoints.

Authenticate via /auth/login to get a JWT token.

Add the token as a Bearer token in the Authorization header to access protected routes.

