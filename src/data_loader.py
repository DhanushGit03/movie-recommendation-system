import pandas as pd

def load_movies(path='data/movies.csv'):
    movies = pd.read_csv(path)
    movies = movies.dropna(subset=['genres'])
    return movies

def load_ratings(path='data/ratings.csv'):
    ratings = pd.read_csv(path)
    return ratings