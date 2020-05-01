import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# dataframe is a 2d matrix rows and columns with index and column names

# example - World population

# Read recently copied text
revenue_df = pd.read_clipboard()
print(revenue_df)
# access index and columns
print(revenue_df.columns)
print(revenue_df['Rank'])
print("\n\n")
print(DataFrame(revenue_df, columns=['Rank', 'Country', 'Med. Age']))

print("\n\n")
# NaN values
revenue_df_2 = DataFrame(revenue_df, columns=['Rank', 'Country', 'Med. Age', 'GDP'])
print(revenue_df_2)

print("\n\n")

# Head and Tail
print(revenue_df.head(1))
print(revenue_df.tail(1))

print("\n\n")
# access rows in dataframe
print(revenue_df.loc[0])  # row 1
print("\n\n")
print(revenue_df.loc[5])  # row 6

print("\n\n")

# assign values to dataframe
# values are assigned to dataframes in their raw format, hence the use of np.arrays

# numpy
array_1 = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4])
revenue_df_2['GDP'] = array_1
print(revenue_df_2)

print("\n\n")

# series
GDP = Series([900, 1000], index=[3, 5])
revenue_df_2['GDP'] = GDP
print(revenue_df_2)

print("\n\n")

# deletion
del revenue_df_2['GDP']
print(revenue_df_2)


print("\n\n")

# dictionary function to dataframe
sample = {
    'Company' : ['A', 'B'],
    'Profit' : [1000, 5000]
}

sample_df = DataFrame(sample)
print(sample)
print("\n\n")
print(sample_df)
