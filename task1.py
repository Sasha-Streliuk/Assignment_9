import pandas as pd
import matplotlib.pyplot as plt

frame = pd.read_csv("titles.csv")
movie_frame = frame[frame.type == 'MOVIE']
show_frame = frame[frame.type == 'SHOW']

movie_imdb = movie_frame.loc[:,'imdb_score']
show_imdb = show_frame.loc[:,'imdb_score']

movie_normalized_df=(movie_imdb - movie_imdb.min())/(movie_imdb.max() - movie_imdb.min())
show_normalized_df=(show_imdb - movie_imdb.min())/(movie_imdb.max() - movie_imdb.min())

fig, axes = plt.subplots(1, 2)
movie_normalized_df.hist(ax = axes[0])
show_normalized_df.hist(ax = axes[1])
plt.show()
