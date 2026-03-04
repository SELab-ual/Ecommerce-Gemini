from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint 1 E-commerce API")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELS ---
class UserLogin(BaseModel):
    email: str
    password: str

class Product(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    price: float
    cover_url: str

# --- MOCK DATA ---
MOCK_PRODUCTS = [
    Product(id=1, title="Advanced Vue.js", author="Jane Doe", isbn="978-1234567890", price=49.99, cover_url="https://via.placeholder.com/150/0000FF/808080?Text=Vue+Book"),
    Product(id=2, title="FastAPI for Beginners", author="John Smith", isbn="978-0987654321", price=39.50, cover_url="https://via.placeholder.com/150/FF0000/FFFFFF?Text=FastAPI+Book"),
]

# --- ENDPOINTS ---
@app.get("/")
def read_root():
    return {"status": "Backend is running"}

@app.post("/api/auth/login")
def login(user: UserLogin):
    # US 554: Mock login logic
    if user.email and user.password:
        return {"message": "Login successful", "token": "mock-jwt-token"}
    raise HTTPException(status_code=400, detail="Invalid credentials")

@app.post("/api/auth/register")
def register(user: UserLogin):
    # US 528: Mock registration
    return {"message": "User registered successfully"}

@app.get("/api/products", response_model=List[Product])
def get_products():
    # US 614, 616, 604: Display products with covers, prices, and bibliographic data
    return MOCK_PRODUCTS

@app.get("/api/search", response_model=List[Product])
def search_products(q: str):
    # US 536, 540: Search functionality
    query = q.lower()
    results = [p for p in MOCK_PRODUCTS if query in p.title.lower() or query in p.author.lower()]
    return results