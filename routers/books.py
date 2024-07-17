from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/books/")
async def read_books(current_user: str = Depends(get_current_user)):
    return [{"title": "Book 1"}, {"title": "Book 2"}]

@router.post("/books/")
async def create_book(book: dict, current_user: str = Depends(get_current_user)):
        return {"title": book["title"], "author": book["author"]}
