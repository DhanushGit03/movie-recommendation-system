# Movie Recommendation System

This repository contains a simple movie recommendation web app built with Streamlit. The app provides movie recommendations for users based on movie genres and user ratings.

## Features

- Content-based movie recommendations using genres and ratings
- Web interface built with Streamlit

## Getting Started

1. **Clone this repository:**
    ```bash
    git clone https://github.com/DhanushGit03/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Set up a Python virtual environment:**
    ```bash
    python -m venv venv
    ```
    - Activate venv(Virtual Environment): `source venv/Scripts/activate`
    - Deactive venv: `deactivate`

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app:**
    ```bash
    streamlit run dashboard/app.py
    ```
    - Open the link shown in your terminal.

## Data

- Place `movies.csv` and `ratings.csv` inside the `data/` folder.
- Sample datasets are available from [MovieLens](https://grouplens.org/datasets/movielens/).

## Notes

- The `venv/` directory is included in `.gitignore` and should not be committed.
- If you use your own datasets, make sure they have the same format as the sample files.