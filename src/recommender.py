import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_genre_matrix(movies):
    # Replace '(no genres listed)' with an empty string
    movies['genres'] = movies['genres'].replace('(no genres listed)', '')
    vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))
    genre_matrix = vectorizer.fit_transform(movies['genres'])
    return genre_matrix, vectorizer

def get_user_profile(user_id, ratings, genre_matrix):
    # Get the indices of movies the user has rated 4.0 or higher
    user_ratings = ratings[ratings['userId'] == user_id]
    top_movies = user_ratings[user_ratings['rating'] >= 4.0]
    if top_movies.empty:
        return None
    indices = top_movies['movieId'].values
    return indices

def recommend_movies(user_id, movies, ratings, genre_matrix, top_n=5):
    rated = ratings[ratings['userId'] == user_id]
    if rated.empty:
        return movies.sample(top_n)
    # Get the indices of the user's top movies
    top_movies = rated[rated['rating'] >= 4.0]
    if top_movies.empty:
        return movies.sample(top_n)
    top_indices = movies[movies['movieId'].isin(top_movies['movieId'])].index
    # Compute the mean vector of genres for user's top movies
    user_profile = genre_matrix[top_indices].mean(axis=0)
    # Fix: Convert user_profile to numpy array to avoid np.matrix error
    user_profile = np.asarray(user_profile)
    # Compute cosine similarity between user profile and all movies
    similarities = cosine_similarity(user_profile, genre_matrix).flatten()
    # Exclude movies already rated by user
    movies['similarity'] = similarities
    recommendations = movies[~movies['movieId'].isin(rated['movieId'])].sort_values('similarity', ascending=False)
    return recommendations[['title', 'genres']].head(top_n)