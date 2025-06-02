# Debug script to test TMDB API connectivity
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

print("=== TMDB API Debug Information ===")
print(f"1. API Key loaded: {TMDB_API_KEY}")
print(f"2. API Key length: {len(TMDB_API_KEY) if TMDB_API_KEY else 'None'}")
print(f"3. API Key type: {type(TMDB_API_KEY)}")

# Test API connectivity with a known movie ID
def test_tmdb_api():
    if not TMDB_API_KEY:
        print("❌ ERROR: TMDB_API_KEY is None or empty")
        return False
    
    # Test with a known movie ID (The Godfather = 238)
    test_movie_id = 238
    url = f"https://api.themoviedb.org/3/movie/{test_movie_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }
    
    print(f"\n4. Testing API call to: {url}")
    print(f"5. Parameters: {params}")
    
    try:
        response = requests.get(url, params=params, timeout=10)
        print(f"6. Response status code: {response.status_code}")
        print(f"7. Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ SUCCESS: API call worked!")
            print(f"8. Movie title returned: {data.get('title')}")
            return True
        else:
            print(f"❌ ERROR: API returned status {response.status_code}")
            print(f"9. Response content: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ ERROR: Request timed out")
        return False
    except Exception as e:
        print(f"❌ ERROR: Exception occurred: {e}")
        return False

# Run the test
test_tmdb_api()

# Additional debugging for your specific function
print("\n=== Testing Your Function ===")

def fetch_tmdb_details_debug(tmdb_id):
    print(f"Testing with tmdb_id: {tmdb_id}")
    
    if not tmdb_id:
        print("❌ tmdb_id is None or empty")
        return None

    try:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}"
        params = {
            "api_key": TMDB_API_KEY,
            "language": "en-US"
        }
        
        print(f"URL: {url}")
        print(f"Params: {params}")

        response = requests.get(url, params=params, timeout=5)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            result = {
                "title": data.get("title"),
                "overview": data.get("overview"),
                "poster_path": f"https://image.tmdb.org/t/p/w500{data.get('poster_path')}" if data.get("poster_path") else None,
                "release_date": data.get("release_date")
            }
            print(f"✅ Success: {result}")
            return result
        else:
            print(f"❌ TMDB API error: {response.status_code} for ID {tmdb_id}")
            print(f"Response: {response.text}")
            return None

    except requests.exceptions.Timeout:
        print(f"❌ TMDB request timed out for movie ID {tmdb_id}")
        return None
    except Exception as e:
        print(f"❌ TMDB request failed for movie ID {tmdb_id}: {e}")
        return None

# Test with a known movie ID
fetch_tmdb_details_debug(238)  # The Godfather