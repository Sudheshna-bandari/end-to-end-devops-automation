from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Review API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    rating: float
    review: str


books = [
    Book(
        id=1,
        title="Atomic Habits",
        author="James Clear",
        rating=5.0,
        review="Excellent book for building good habits."
    ),
    Book(
        id=2,
        title="Clean Code",
        author="Robert C. Martin",
        rating=4.5,
        review="Useful programming practices."
    )
]


@app.get("/")
def home():
    return {
        "message": "Book Review API is running",
        "version": "1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:
        if book.id == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


@app.post("/books")
def add_book(book: Book):

    books.append(book)

    return {
        "message": "Book added successfully",
        "book": book
    }


@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for book in books:
        if book.id == book_id:
            books.remove(book)

            return {
                "message": "Book deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )