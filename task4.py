import pandas as pd

movies = pd.read_csv('titles.csv')
actors = pd.read_csv('credits.csv')

movies = movies[['id', 'imdb_score']]
movies = movies.dropna(subset=['imdb_score'])
movies = movies.sort_values(by=['imdb_score'], ascending=False)[:1000]

actors = actors[['id', 'name']]
actors = actors.dropna()
actors = actors.loc[actors['id'].isin(movies['id'])]
actors = actors.groupby(['name']).size().nlargest(10).reset_index(name='top10')

print(actors)
