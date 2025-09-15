from fastapi import FastAPI, Query
from data_processing import library_data, Book
from constants import CURRENT_YEAR
from pprint import pprint

app = FastAPI()

library = library_data("library.json")
books = library.books

# print(library) test to see data

@app.get("/books")
async def read_books():
    return books

# in terminal uvicorn api:app --reload
# opens localhost, then navigate to /books to see json library

@app.get("/books/")
async def filter_books(
    start_year: int= Query(
        1950,
        gt=1500,
        lt=CURRENT_YEAR + 1,
        description = "Filter books that are newer than this year"
    )
):
    filtered_books = [book for book in books if start_year < book.year]
    return filtered_books


#read_book_by_title(title: str):
#   return [book for book in books if book.title.casefold()== title.casefold()]

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
#async def update_book(book_request:Book)
    




#uv pip install fastapi uvicorn
# uvicorn api:app --reload (name of file:name of app --reload (so it keeps changing from that directory, no need to run it again))
