import pandas as pd

data = {
    'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom', 'Harry'],
    'rank': [4, 1, 3, 5, 2, 6],
}

df = pd.DataFrame(data, index=data['name'])

num = int(input())

print(df[df['rank'] == num]['name'])