from fastapi import FastAPI
from pydantic_ai import Agent 
from dotenv import load_dotenv
from utils import query_duckdb
from data_models import Movie, Prompt


load_dotenv()

agent= Agent(model="google-gla:gemini-2.5-flash", output_type=Movie)

app= FastAPI()

@app.get("/movies")
async def read_movies():
    movies = query_duckdb("FROM movies;") # 'FROM movies;' = SELECT* in duckdb
    return movies.to_dict(orient="records")

@app.post("/movie")
async def create_movie(query: Prompt):
    result = await agent.run(query.prompt)  
    movie = result.output

    # to enter movies into db data/movies.duckdb :
    query_duckdb(
        "INSERT INTO movies VALUES (?,?,?,?)",
        parameters=(movie.title, movie.year, movie.genre, movie.rating)
    )

    return movie

    #return movie
    #- to just see unstructured output

    # then go into POST to post questions (do a few) then GET to see results as in db
    # check in terminal, navigate to parentfolder (dep on your setup) duckdb data/movies.duckdb
    # then do from movies; to see populated duckdb df
    # next step: consume to frontend





# to run with old uv:
# 'uvicorn movies_api:app --reload'

# with new uv run:
# 'uv run uvicorn movies_api:app --reload'