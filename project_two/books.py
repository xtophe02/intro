from fastapi import FastAPI
from .books_data import BOOKS
from .book_class import Book, NewBook

app = FastAPI()


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return BOOKS[book_id - 1]


@app.get("/books/publish/{date}")
async def read_book_by_date(date: str):
    return [book for book in BOOKS if book.published_year == date]


@app.get("/books/")
async def read_book_by_rating(rating: int):
    return [book for book in BOOKS if book.rating == rating]


@app.post("/create_book")
async def create_book(new_book: NewBook):
    new_book = Book(**new_book.model_dump())
    new_book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    BOOKS.append(new_book)


@app.put("/update_book")
async def update_book(book: NewBook):
    for i, b in enumerate(BOOKS):
        if b.id == book.id:
            BOOKS[i] = Book(**book.model_dump())
            return BOOKS[i]


@app.delete("/delete_book")
async def delete_book(book_id: int):
    for i, b in enumerate(BOOKS):
        if b.id == book_id:
            del BOOKS[i]
            return b
    return None
