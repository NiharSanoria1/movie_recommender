import requests
import os
from dotenv import load_dotenv

# Load the TMDB API key/token from .env file
load_dotenv('.env')

TMDB_BEARER_TOKEN = os.getenv("TMDB_BEARER_TOKEN")  # NOTE: this should be the access token, not the API key

def fetch_tmdb_details(tmdb_id):
    if not tmdb_id:
        return None

    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_BEARER_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        print(response.text)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "title": data.get("title"),
                "overview": data.get("overview"),
                "poster_path": f"https://image.tmdb.org/t/p/w500{data.get('poster_path')}" if data.get("poster_path") else None,
                "release_date": data.get("release_date"),
                "rating" : data.get("vote_average")
            }
        else:
            print(f"TMDB API error: {response.status_code} for ID {tmdb_id}")
            return None

    except requests.exceptions.Timeout:
        print(f"TMDB request timed out for movie ID {tmdb_id}")
        return None
    except Exception as e:
        print(f"TMDB request failed for movie ID {tmdb_id}: {e}")
        return None
