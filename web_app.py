import streamlit as st
import requests
from recomend import movies

API_URL = "http://127.0.0.1:8000/recommend"

st.header("🎬 Movie Recommender System")

movie_list = movies["title"].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button("Show Recommendation"):
    try:
        response = requests.get(API_URL, params={"movie": selected_movie})
        response.raise_for_status()

        data = response.json()
        recommendations = data.get("recommendations", [])

        st.subheader("Recommended Movies:")

        if not recommendations:
            st.warning("No recommendations found.")
        else:
            for rec_movie in recommendations:
                st.write("🎥", rec_movie)

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching recommendations: {e}")
