import pandas as pd

# Load datasets
movies_df = pd.read_csv("data/processed/movies_and_genres_hot_encoded_df.csv")  # has 'movieId', 'title'
links_df = pd.read_csv("data/raw/links.csv")  # has 'movieId', 'tmdbId'

# Merge on 'movieId'
merged_df = pd.merge(movies_df[['movieId', 'title']], links_df[['movieId', 'tmdbId']], on='movieId')

# Drop rows with missing tmdbId
merged_df = merged_df.dropna(subset=['tmdbId'])

# Optional: Convert tmdbId to int (some are float)
merged_df['tmdbId'] = merged_df['tmdbId'].astype(int)

# Save mapping for use in Streamlit app
merged_df.to_csv("data/processed/movie_id_mapping.csv", index=False)
print("Mapping saved to data/processed/movie_id_mapping.csv")
