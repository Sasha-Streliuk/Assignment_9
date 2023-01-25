import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab

frame = pd.read_csv("titles.csv")
movie_frame = frame[frame.type == 'MOVIE']
show_frame = frame[frame.type == 'SHOW']

movie_imdb = movie_frame.loc[:,'imdb_score']
show_imdb = show_frame.loc[:,'imdb_score']


plt.subplot(2, 2, 1)
plt.hist(movie_imdb, np.arange(0,10,0.2))
plt.subplot(2, 2, 2)
plt.hist(show_imdb, np.arange(0,10,0.2))
plt.show()
