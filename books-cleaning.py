import pandas as pd

bookData = pd.read_csv('data/Books.csv')
ratingsData = pd.read_csv('data/Ratings.csv')
usersData = pd.read_csv('data/Users.csv')

mergedISBN = pd.merge(bookData, ratingsData, how='inner', left_on='ISBN', right_on='ISBN')
mergedUser = pd.merge(mergedISBN, usersData, how='inner', left_on='User-ID', right_on='User-ID')

mergedUser.to_csv('data/mergedData.csv', sep='\t')
columnsDrop = ['Image-URL-S', 'Image-URL-M', 'Image-URL-L']
merged = mergedUser.drop(columns=columnsDrop, axis=1)
merged = merged.dropna()
merged.to_csv('data/totalData.csv', sep='\t')

print(merged.head())
