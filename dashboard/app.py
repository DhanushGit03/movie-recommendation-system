import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from src.data_loader import load_movies, load_ratings
from src.recommender import build_genre_matrix, recommend_movies

st.title("🎬 Movie Recommendation System")

# Load data
movies = load_movies()
ratings = load_ratings()
genre_matrix, _ = build_genre_matrix(movies)

user_ids = ratings['userId'].unique()
user_id = st.selectbox("Select User ID", options=sorted(user_ids))

if st.button("Show Top 5 Recommendations"):
    recommendations = recommend_movies(user_id, movies.copy(), ratings, genre_matrix)
    st.write("**Top 5 Movie Recommendations:**")
    st.table(recommendations.reset_index(drop=True))