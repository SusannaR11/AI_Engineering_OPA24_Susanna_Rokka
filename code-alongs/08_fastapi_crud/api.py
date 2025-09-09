from fastapi import FastAPI
from data_processing import library_data, Book

app = FastAPI()

library = library_data("library.json")
books = library.books

# print(library) test to see data

@app.get("/books")
async def read_books():
    return books

# in terminal uvicorn api:app --reload
# opens localhost, then navigate to /books to see json library

@app.get("/books/title/{title}")
async def read_book_by_title(title: str):
    return [book for book in books if book.title.casefold()== title.casefold()]

# /docs to see endpoints in Swagger
# try it out , execute

# copy curl command paste in terminal: 
# susannarokka@Susannas-MacBook-Pro AI_Engineering_OPA24_Susanna_Rokka % curl -X 'GET' \
#  'http://127.0.0.1:8000/books' \
#  -H 'accept: application/json'
# to see results

# test endpoints and see request url's

@app.post("/books/create_book")
async def create_book(book_request: Book):
    new_book = Book.model_validate(book_request)
    books.append(new_book)

    return new_book
#UPDATE (do a to-do list...) so far data is not persistent ie not saved in json file. 
# it's in short term memory
# 

# TODO : UPDATE
# DELETE
# QUERY PARAMETERS

# @app.put("/books")
