import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

insurance = pd.read_csv('data/insurance.csv')

print(insurance['smoker'].unique())

sns.catplot(data=insurance, x='smoker', y='charges', kind='violin')

sns.catplot(data=insurance, x='smoker', y='charges', kind='strip')  # 데이터를 하나하나 볼 수 있음

print(insurance['sex'].unique())

sns.catplot(data=insurance, x='smoker', y='charges', kind='strip', hue='sex')
# hue: 색을 의미, 프로세스에 따라 색이 달라짐
sns.catplot(data=insurance, x='smoker', y='charges', kind='swarm', hue='sex') # swarm: 데이터들이 겹치지 않고 펴짐
plt.show()