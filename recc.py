import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie dataset
data = {'Title': ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4'],
        'Genre': ['Action', 'Comedy', 'Action, Thriller', 'Comedy, Romance']}
movies_df = pd.DataFrame(data)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Replace NaN with an empty string
movies_df['Genre'] = movies_df['Genre'].fillna('')

# Compute TF-IDF matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Genre'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies_df.index[movies_df['Title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:3]  # Get top 2 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['Title'].iloc[movie_indices]

# Get recommendations for a movie
movie_title = 'Movie 1'
recommendations = get_recommendations(movie_title)
print(f"Recommended movies for '{movie_title}': {', '.join(recommendations)}")