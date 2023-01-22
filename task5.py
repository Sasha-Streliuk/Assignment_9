import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('titles.csv')
movies = movies[['id', 'imdb_score', 'genres']]
movies = movies.dropna(subset=['imdb_score'])
movies = movies.sort_values(by=['imdb_score'], ascending=False)[:1000]

movies["genres"] = movies["genres"].apply(lambda x: x.replace("[", "").replace("]", ""))
genres = movies['genres'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
genres.value_counts().plot(kind='bar')
plt.show()
