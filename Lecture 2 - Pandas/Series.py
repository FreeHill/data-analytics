import pandas as pd
from pandas import Series
import numpy as np

object = Series([5, 10, 15, 20])
print(object)

print(object.values)
print(object.index)

# use numpy array for series
data_array = np.array(['a', 'b', 'c'])
s = Series(data_array)
print(s.index)

# custom index
s = Series(data_array, index=[100, 101, 102])
print(s)

print('********\n\n********')
# real world example
revenue = Series([28, 80, 40, 35], index=['ola', 'uber', 'grab', 'gojek'])
print(revenue['ola'])
print(revenue[revenue >= 35])

# use boolean conditions
print('\n', 'ola' in revenue)

revenue_dict = revenue.to_dict()
print('\n',revenue_dict)

# NaN values
index_2 = ['ola', 'uber', 'grab', 'gojek', 'lyft']
revenue_2 = Series(revenue, index_2)
print('\n', revenue_2)
# Check for a null value in your array
print('\n', pd.isnull(revenue_2))
print('\n', pd.notnull(revenue_2))

# addition of Series
print('\n', revenue_2 + revenue)

# assigning names
revenue_2.name = 'Company Revenues'
revenue_2.index.name = 'Company Name'
print('\n', revenue_2)