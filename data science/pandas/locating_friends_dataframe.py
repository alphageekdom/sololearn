import pandas as pd

data = {
    'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom'],
    'number': ['1234', '5678', '2222', '1111', '0909'],
}

n = input()
df = pd.DataFrame(data, index= data['name'])
print(df.loc[n])