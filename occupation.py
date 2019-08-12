import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

job = pd.read_csv('data/occupation.csv')

f = job[job['gender'] == 'F']
print(f['occupation'].value_counts().sort_values(ascending=False))

m = job[job['gender'] == 'M']
print(m['occupation'].value_counts().sort_values(ascending=False))