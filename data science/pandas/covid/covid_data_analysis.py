import pandas as pd

df = pd.read_csv('./ca-covid.csv')

df.drop('state', axis=1, inplace=True)
df.set_index('data', inplace=True)

df['ratio'] = df['deaths'] / df['cases']

print(df[df['ratio'] == df['ratio'].max()])