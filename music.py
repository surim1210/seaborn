import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

music = pd.read_csv('data/music.csv')

get = music.corr()['Getting up']
sns.heatmap(get.corr(), annot=True)
plt.show()
print(get[1:19].sort_values(ascending=False))
