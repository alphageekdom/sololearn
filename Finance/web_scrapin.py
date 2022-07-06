import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
data = pd.read_html(url, flavor='html5lib')

df = data[0]
df = df[['Symbol', 'Security']]
print(df)