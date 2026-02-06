from fastapi import FastAPI
from recomend import recommend
from fastapi import FastAPI, HTTPException


app = FastAPI()

@app.get("/recommend")
def get_recommendation(movie: str):
    result = recommend(movie)

    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Movie '{movie}' not found in dataset"
        )

    return {
        "movie": movie,
        "recommendations": result
    }


@app.get("/")
def root():
    return {"status": "Movie Recommender API running"}