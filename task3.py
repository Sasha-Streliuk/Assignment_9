import pandas as pd
import matplotlib.pyplot as plt

frame = pd.read_csv("titles.csv")

sorted_frame = frame[frame.release_year > 2000]
sorted_frame_imdb8 = sorted_frame[sorted_frame.imdb_score > 8.0]

rating_8 = sorted_frame["release_year"].value_counts()
rating_less8 = sorted_frame_imdb8["release_year"].value_counts()

rating_sort_8 = rating_8.sort_index(ascending=True)
rating_sort_less8 = rating_less8.sort_index(ascending=True)

percent = rating_sort_8 / rating_sort_less8
print(percent.idxmax())

plt.plot(range(len(percent.keys())), percent.values)
plt.xticks(range(len(percent.keys())), percent.keys())
plt.show()
