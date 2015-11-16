'''
Created on 16 Nov 2015
@author: charlotto
'''
import pandas as pd
import sklearn

# Column headers to make things a bit easier later on
cols = ['ID', 'Price', 'Date', '4', 'PropType', '6', 'LeaseDuration',
        '8', '9', '10', '11', 'Location', '13', '14', '15', '16']

# Read in training data
data = pd.read_csv(open('testing.csv'), header=None, names=cols)

# Convert into pandas data frame
pData = pd.DataFrame(data)
# Get data into object "Bunch"
type(pData)

# Lets start with the location feature
feature_cols = ['Location']

# Features matrix(n_samples,n_features)
X = pData[feature_cols]
# Response/target vector
y = pData['Price']

# Modelling process now!
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)




