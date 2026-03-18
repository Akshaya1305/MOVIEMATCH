# ============================================
# CineMatch — Movie Recommendation System
# recommendation.py — ML Model
# ============================================

import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---- Load & Prepare Data ----
# Load movies dataset
movies = pd.read_csv('movies.csv')

# Load credits dataset
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge both datasets on title
df = movies.merge(credits, on='title')

# Keep needed columns
df = df[['title', 'overview', 'genres', 'keywords',
         'vote_average', 'release_date', 'runtime',
         'cast', 'crew']]

# Handle missing values
df = df.fillna('')

# ---- Helper Functions ----

def extract_genres(genres_str):
    """Extract genre names from JSON string"""
    try:
        genres = json.loads(genres_str.replace("'", '"'))
        return [g['name'] for g in genres]
    except:
        return []

def extract_cast(cast_str):
    """Extract top 5 cast names from JSON string"""
    try:
        import ast
        cast = ast.literal_eval(cast_str)
        return [c['name'] for c in cast[:5]]
    except:
        return []

def extract_director(crew_str):
    """Extract director name from crew JSON string"""
    try:
        import ast
        crew = ast.literal_eval(crew_str)
        for member in crew:
            if member['job'] == 'Director':
                return member['name']
        return 'Unknown'
    except:
        return 'Unknown'

def get_release_year(date_str):
    """Extract year from date string"""
    try:
        return str(date_str)[:4]
    except:
        return 'Unknown'

def get_ott_platforms(title):
    """Returns OTT platforms for popular movies"""
    ott_map = {
        'avengers': ['Disney+ Hotstar'],
        'iron man': ['Disney+ Hotstar'],
        'the dark knight': ['Netflix'],
        'avatar': ['Disney+ Hotstar'],
        'inception': ['Netflix', 'Amazon Prime'],
        'titanic': ['Amazon Prime', 'Netflix'],
        'interstellar': ['Amazon Prime'],
        'the avengers': ['Disney+ Hotstar', 'Netflix'],
        'batman begins': ['Netflix'],
        'spider-man': ['Netflix', 'Amazon Prime'],
        'joker': ['Amazon Prime', 'Netflix'],
        'thor': ['Disney+ Hotstar'],
        'captain america': ['Disney+ Hotstar'],
        'guardians of the galaxy': ['Disney+ Hotstar'],
        'jurassic park': ['Amazon Prime'],
        'the matrix': ['Netflix', 'Amazon Prime'],
        'forrest gump': ['Amazon Prime'],
        'the lion king': ['Disney+ Hotstar'],
        'toy story': ['Disney+ Hotstar'],
        'finding nemo': ['Disney+ Hotstar'],
    }
    title_lower = title.lower()
    for key in ott_map:
        if key in title_lower:
            return ott_map[key]
    return ['Check Netflix', 'Check Amazon Prime']

# ---- Feature Engineering ----
df['combined'] = df['overview'] + ' ' + df['genres'] + ' ' + df['keywords']
df['title_lower'] = df['title'].str.lower()

# ---- Build ML Model ----
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])
similarity = cosine_similarity(tfidf_matrix)

# ---- Recommendation Function ----
def get_recommendations(movie_title):
    """Returns 5 similar movies"""
    movie_title_lower = movie_title.strip().lower()

    if movie_title_lower not in df['title_lower'].values:
        return ["Movie not found! Please check the spelling."]

    movie_index = df[df['title_lower'] == movie_title_lower].index[0]
    similarity_scores = list(enumerate(similarity[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_movies = similarity_scores[1:6]

    return [df['title'].iloc[i] for i, score in top_movies]


# ---- Movie Detail Function ----
def get_movie_details(movie_title):
    """Returns full details of a movie"""
    movie_title_lower = movie_title.strip().lower()

    if movie_title_lower not in df['title_lower'].values:
        return None

    movie = df[df['title_lower'] == movie_title_lower].iloc[0]

    return {
        'title': movie['title'],
        'overview': movie['overview'],
        'genres': extract_genres(movie['genres']),
        'cast': extract_cast(movie['cast']),
        'director': extract_director(movie['crew']),
        'rating': round(float(movie['vote_average']), 1) if movie['vote_average'] != '' else 'N/A',
        'year': get_release_year(movie['release_date']),
        'runtime': str(int(float(movie['runtime']))) + ' min' if movie['runtime'] != '' else 'N/A',
        'ott': get_ott_platforms(movie['title'])
    }


# ---- Test ----
if __name__ == '__main__':
    movie = input("Enter a movie name: ")
    results = get_recommendations(movie)
    print("\n🎬 Recommended Movies:")
    for i, title in enumerate(results, 1):
        print(f"{i}. {title}")

    details = get_movie_details(movie)
    if details:
        print(f"\n📋 Movie Details:")
        print(f"Director: {details['director']}")
        print(f"Cast: {', '.join(details['cast'])}")
        print(f"Genres: {', '.join(details['genres'])}")
        print(f"Rating: {details['rating']}/10")
        print(f"Year: {details['year']}")
        print(f"Runtime: {details['runtime']}")
        print(f"OTT: {', '.join(details['ott'])}")