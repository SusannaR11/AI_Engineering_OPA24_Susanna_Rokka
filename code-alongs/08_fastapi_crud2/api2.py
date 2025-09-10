from fastapi import FastAPI, Query, HTTPException
from data_processing2 import library_data, Book
from pprint import pprint
from constants2 import CURRENT_YEAR

library = library_data("library.json")
books= library.books

pprint(books) # list of books sorted by id

app = FastAPI()

@app.get("/books")
async def read_books():
    return books

# path parameter
@app.get("/books/title/{title}")
async def read_book_by_title(title:str):
    return (book for book in books if book.title.casefold() == title.casefold())

# query parameter - ?start_year=1950
@app.get("/books/")
async def filter_books(
    start_year: int = Query(
        1950, 
        gt= 1500, 
        lt= CURRENT_YEAR + 1,
        description="Filters books that are newer than this year"
    ),
    author: str = Query(None, description="Filter by author's firstname and lastname")
):
    filtered_books = [book for book in books if start_year < book.year]

    if author:
        filtered_books = [
        book for book in filtered_books
        if author.casefold() == book.author.casefold()]
    return filtered_books

@app.post("/books/create_book")
async def create_book(book_request: Book):
    new_book = Book.model_validate(book_request)
    books.append(new_book)

    return new_book

# loan books for library
@app.post("/books/borrow_book/{id}")
async def borrow_book(id: int):
    book = next((b for b in books if b.id == id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="item not found")
    
    if book.number_copy <= 0:
        raise HTTPException(status_code=400, detail="Inga exemplar kvar att låna")
    book.number_copy -= 1
    return{
        "message": f"Du har lånat '{book.title}'.",
        "copies_left": book.number_copy
    }

#update

@app.put("/books/update_book")
async def update_book(updated_book: Book):
    for i, book in enumerate(books):
        if book.id == updated_book.id:
            books[i] == updated_book
    return updated_book


# delete book

@app.delete("/books/delete_book/{id}")
async def delete_book(id: int):
    for i, book in enumerate(books):
        if book.id == id:
            del books[i]
            break
  
#uv pip install fastapi uvicorn
# uvicorn api:app --reload


# cmd k + c 
# cmd k + u