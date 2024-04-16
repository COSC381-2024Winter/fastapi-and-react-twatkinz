from typing import Union
from fastapi import FastAPI
from movies import Movies

movies = Movies('./movies.txt')
app = FastAPI()

@app.get("/movies/{movie_id}")
def read_item(movie_id: int):
    for i in movies._movies:
            if movie_id is i['id']:
                return(i)
    else:
        return{None}
    