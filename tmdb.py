import requests
import os

API_KEY = os.getenv("TMDB_API_KEY")  # recommended
BASE_URL = "https://api.themoviedb.org/3"

def fetch_poster(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"

    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # IMPORTANT

    data = response.json()
    poster_path = data.get("poster_path")

    if not poster_path:
        return None

    return f"https://image.tmdb.org/t/p/w500{poster_path}"
