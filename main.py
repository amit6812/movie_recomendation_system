from fastapi import FastAPI, HTTPException
from recomend import recommend

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Movie Recommender API running"}


@app.get("/ping")
def ping():
    """
    Simple health check endpoint.
    Returns 200 OK if API is running.
    """
    return {"status": "alive"}


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


@app.get("/invoke")
def invoke(movie: str = None):
    """
    Generic invocation endpoint.
    Can be used to test the recommendation function or trigger some action.
    If a movie is provided, returns recommendations.
    """
    if not movie:
        return {"message": "No movie provided for invocation."}

    result = recommend(movie)
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Movie '{movie}' not found in dataset"
        )

    return {
        "invoked_movie": movie,
        "recommendations": result
    }


# Run with custom host and port
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web_app:app", host="0.0.0.0", port=8080, reload=True)
