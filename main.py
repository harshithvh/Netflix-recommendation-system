# Upload the dataset
# Reading dataset
import pandas as pd

movies = pd.read_csv('movies.csv')
movies.head(2)
print(movies.info())

# Dropping not required columns
required_columns =['title','original_title', 'tagline', 'keywords', 'overview', 'genres', 'cast', 'director']
movies = movies[required_columns]
print(movies.isna().sum())

movies.fillna(' ', inplace=True)
print(movies.isna().sum())
print(movies.iloc[0])

# Create movie CONTENT
movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['director'] = movies['director'].apply(lambda x: x.replace(" ","") )

# Converting List to Strings
movies['genres'] = movies['genres'].apply(lambda x: ','.join(map(str, x)))
movies['keywords'] = movies['keywords'].apply(lambda x: ','.join(map(str, x)))
movies['cast'] = movies['cast'].apply(lambda x: ','.join(map(str, x)))

movies['content'] = movies['title'] + ' ' + movies['overview'] + ' ' + movies['keywords'] + ' ' + movies['cast'] + ' ' + movies ['director']
print(movies['content'])

# Natural Language Processing
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=1000)
movie_vectors = vectorizer.fit_transform(movies['content'].values) 

# Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(movie_vectors)
similarity_df = pd.DataFrame(similarity)
print(similarity_df)

# Recommending Movies
def recommend(movie):
    # find movie index from dataset
    movies_index = movies[movies['title'] == movie].index[0]
    
    # finding cosine similarities of movie
    distances = similarity[movies_index]
    
    # sorting cosine similarities
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    for i in movies_list:
        print(movies.iloc[i[0]].title)
print(movies.title.head(10))
print('')
print(recommend('Harry Potter and the Half-Blood Prince'))