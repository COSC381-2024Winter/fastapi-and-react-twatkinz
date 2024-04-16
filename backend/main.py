from fastapi import FastAPI
from movies import Movies
from pydantic import BaseModel


movies = Movies('./movies.txt')
app = FastAPI()

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
