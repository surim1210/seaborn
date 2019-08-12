import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey = pd.read_csv('data/survey.csv')

poem = survey.corr().loc['Musical instruments', 'Writing']  # corr: 상관관계
looks = survey.corr().loc['Spending on looks', 'Branded clothing']
memo = survey.corr().loc['Writing notes', 'New environment']
work = survey.corr().loc['Workaholism', 'Healthy eating']


print('1. ', poem)
print('2. ', looks)
print('3. ', memo)
print('4. ', work)

