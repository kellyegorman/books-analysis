import pandas as pd

bookData = pd.read_csv('books.csv')
ratingsData = pd.read_csv('ratings.csv')
usersData = pd.read_csv('users.csv')

mergedISBN = pd.merge(bookData, ratingsData, how='inner', left_on='ISBN', right_on='ISBN')
mergedUser = pd.merge(mergedISBN, usersData, how='inner', left_on='User-ID', right_on='User-ID')

mergedUser.to_csv('mergedData.csv', sep='\t')
columnsDrop = ['Image-URL-S', 'Image-URL-M', 'Image-URL-L']
merged = mergedUser.drop(columns=columnsDrop, axis=1)
merged = merged.dropna()
merged.to_csv('totalData.csv', sep='\t')

print(merged.head())
