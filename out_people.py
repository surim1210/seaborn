import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

out_df = pd.read_csv('data/subway.csv')

sns.kdeplot(out_df['out'])
plt.show()