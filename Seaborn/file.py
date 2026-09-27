import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Dataset Cleaning\modified_data.csv')
# print(df.info())
df1=df.select_dtypes(include=['int64','float'])
# print(df1.info())

## Heatmap
# sns.heatmap(df1.corr(),annot=True)
# plt.show()

## Pairplot
sns.pairplot(df1)
plt.show()