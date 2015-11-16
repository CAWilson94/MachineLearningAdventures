'''
Created on 16 Nov 2015
@author: charlotto
'''
import pandas as pd

cols = ['ID', 'Price', 'Date', '4', 'PropType', '6', 'LeaseDuration',
        '8', '9', '10', '11', 'Location', '13', '14', '15', '16']
data = pd.read_csv(open('testing.csv'), header=None, names=cols)
# Convert into pandas data frame so I can get the column names
pData = pd.DataFrame(data)
print data.columns
# print data.columns
type(pData)

# Lets start with the location feature
feature_cols = ['Location']
X = pData[feature_cols]
y = pData['Price']
print y
