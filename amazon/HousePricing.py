'''
Created on 16 Nov 2015
@author: charlotto
'''
import pandas as pd
from sklearn.feature_extraction import DictVectorizer as DV

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
feature_cols = pData['Location']

"""
Convert the features into a list of dicts, i.e. convert
the Location Column into dicts.
Then create a new dataframe containing only these columns

DataFrame has a toDict() method, however, the keys are columns.
So we transpose the data frame then call the dict to values method
"""

# Lets try the pandas way
# Just using this to create dict values for scikit learns vectorizer thingy
panda = feature_cols
panda_dict = panda.T.to_dict().values()

print panda_dict
# Now to convert the strings..
#vectorizer = DV( sparse = False )
#vec_X_train = vectorizer.fit_transform(panda_dict)


# Features matrix(n_samples,n_features)
# 
# print X

# Response/target vector
#y = pData['Price']

"""
# Modelling process now!
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)

"""


