import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

salaries = pd.read_csv('data/salaries.csv')

sns.violinplot(salaries['salary'])   # 대칭그래프
sns.distplot(salaries['salary'], bins=15)    # 히스토그램위에 kde곡성
plt.show()