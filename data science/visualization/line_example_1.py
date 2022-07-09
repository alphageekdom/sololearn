import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./ca-covid.csv')
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%y')
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

(df[df['month']==12])[['cases', 'deaths']].plot()
plt.savefig('cases_deaths_line_plot.png')