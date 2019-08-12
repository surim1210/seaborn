import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

exam = pd.read_csv('data/exam.csv')

print(exam.corr())
sns.heatmap(exam.corr(), annot=True)

'''
색이 밝을수록 상관 계수가 더 높다는 의미
<annot=True>를 추가하면 숫자도 함께 보여줌
'''
plt.show()
