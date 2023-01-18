import pandas as pd
import matplotlib.pyplot as plt

frame = pd.read_csv("titles.csv")
age = frame.loc[:,"age_certification"]

shows_amount = age.value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(shows_amount, labels=shows_amount.keys(), autopct='%1.1f%%',
        startangle=90, textprops={'fontsize': 6})
ax1.axis('equal')  

plt.show()