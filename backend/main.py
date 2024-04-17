from fastapi import FastAPI
from movies import Movies
from pydantic import BaseModel



movies = Movies('./movies.txt')
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Movie(BaseModel):
    name: str
    cast: list


@app.get("/movies/{movie_id}")
def read_movie(movie_id: int):
    for i in movies._movies:
            if movie_id is i['id']:
                return(i)
    else:
        return{None}
    

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: Movie):
    for i in movies._movies:
        if movie_id is i['id']:
            i['name'] = movie.name
            i['cast'] = movie.cast
            return {
                    "movie_name": i['name'],
                    "movie_cast": i['cast'],
                    "movie_id": i['id']
                }
    else:
        return{None}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    for i, movie in enumerate(movies._movies):
        if movie_id is movie['id']:
            deleted_movie = movies._movies[i]
            del movies._movies[i]
            return {
                    "movie_name": deleted_movie['name'],
                    "movie_cast": deleted_movie['cast'],
                    "movie_id": deleted_movie['id']
                }


@app.post("/movies/add")
def add_movie(movie: Movie):
    new_movie = movies.add_movie(movie.name, movie.cast)
    return new_movie