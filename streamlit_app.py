import os 
import sys
import streamlit as st
import pandas as pd

from python_scripts.movie_recommender import movie_recommender, cosine_sim_df
from python_scripts.fetch_tmdb_details import fetch_tmdb_details

# importing mapped data
mapping_df = pd.read_csv("data/processed/movie_id_mapping.csv")

# Helper to get tmdbId
def get_tmdb_id(title):
    row = mapping_df[mapping_df["title"] == title]
    if not row.empty:
        return row.iloc[0]["tmdbId"]
    return None

st.title("🎬 Movie Recommender System")
st.markdown("A content-based recommendation engine using genre similarity (MovieLens 100k).")

# Let user select from available movies
movie_list = cosine_sim_df.index.tolist()

# Search input
search_term = st.text_input("🔍 Search for a movie by title:")
# Filter movie list by search term
filtered_list = [m for m in movie_list if search_term.lower() in m.lower()] if search_term else movie_list
# Dropdown for filtered list
selected_movie = st.selectbox("🎞️ Select a movie you like:", filtered_list)


# Get number of recommendations
top_n = st.slider("Number of recommendations:", 1, 20, 5)

# Recommend when button is clicked
if st.button("Recommend"):
    with st.spinner("Finding similar movies..."):
        recommendations = movie_recommender(selected_movie, top_n=top_n)
        
    st.success(f"Top {top_n} recommendations for **{selected_movie}**:")
    
    cols = st.columns(2)
    for i, movie in enumerate(recommendations, 1):
        tmdb_id = get_tmdb_id(movie)
        details = fetch_tmdb_details(tmdb_id) if tmdb_id else None

        if details:
            with cols[i % 2]:
                st.markdown(f"#### {details['title']} ({details['release_date'][:4] if details['release_date'] else 'N/A'})")
                st.markdown(f"[🔗 View on TMDB](https://www.themoviedb.org/movie/{tmdb_id})")
                if details["poster_path"]:
                    st.image(details["poster_path"], width=200)
                st.caption(details["overview"][:250] + "..." if details["overview"] else "No description.")
                st.write(f"⭐ Rating: {details['rating']}/10")
