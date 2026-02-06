import pickle
import pandas as pd
import os

# Load movies
movie_path = os.path.dirname('movie_dict.pkl')
movies = pickle.load(open(os.path.join(movie_path, 'movie_dict.pkl'), 'rb'))
movies = pd.DataFrame(movies)

# Load similarity matrix
similarity_path = os.path.dirname('similarity.pkl')
similarity = pickle.load(open(os.path.join(similarity_path, 'similarity.pkl'), 'rb'))

def recommend(movie_title):
    matches = movies[movies['title'].str.contains(movie_title, case=False)]
    if matches.empty:
        return []

    index = matches.index[0]

    # Get top 5 similar movies
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    # ONLY return titles (no posters)
    recommendations = [{"title": movies.iloc[i[0]].title} for i in distances[1:6]]

    return recommendations
