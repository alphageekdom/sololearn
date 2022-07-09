import pandas as pd

df = pd.read_csv('./ca-covid.csv')
df.set_index('date', inplace=True)
df.drop('state', axis=1, inplace=True)

print(df.head())

df.info()