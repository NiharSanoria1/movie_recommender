import os
base_dir = os.path.dirname(os.path.dirname(__file__))

import numpy as np
import pandas as pd

data_path = os.path.join(base_dir, "data", "processed" , "cosine_sim_dataframe.csv")
cosine_sim_df = pd.read_csv(data_path, index_col=0)

df_data_path = os.path.join(base_dir , "data", "processed", "movies_and_genres_hot_encoded_df.csv")
movies = pd.read_csv(df_data_path)

cosine_matrix_data_path = os.path.join(base_dir, "data", "processed", "cosine_sim_matrix.npy")
cosine_sim_matrix= np.load(cosine_matrix_data_path)


def movie_recommender(movie_name , top_n = 5):
    
    if movie_name not in cosine_sim_df.index:
        print(f"Movie '{movie_name}' not found in the dataset.")
        return []
    
    # Get similarity scores for all movies compared to the given movie
    similarities = cosine_sim_df.loc[movie_name]
    
     # Sort scores in descending order and drop the movie itself
    recommendations = similarities.sort_values(ascending=False).drop(movie_name).head(top_n)
    
    # Return the movie titles as a list
    return recommendations.index.tolist()