import pandas as pd

df = pd.read_csv('./ca-covid.csv')

df.drop('state', axis=1, inplace=True)
df['month'] = pd.to_datetime(df['date'], format='%d.%m.%y').dt.month_name()
df.set_index('date', inplace=True)

# group data by month
print(df['month'].value_counts())
print('\n')
# group data by month and calculate sum
print(df.groupby('month')['cases'].sum())
print('\n')

# calculate number of total cases
print(df['cases'].sum())