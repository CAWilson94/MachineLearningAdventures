"""
November 2015
@author Charlotte Alexandra Wilson 

"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# Column headers to make things a bit easier later on
cols = ['ID', 'Price', 'Date', '4', 'PropType', '6', 'LeaseDuration',
        '8', '9', '10', '11', 'Location', '13', '14', '15', '16']

# Read in training & testing data
# data = pd.read_csv(open('training.csv'), header=None, names=cols)
data = pd.read_csv(open('testing.csv'), header=None, names=cols)

# Convert into pandas data frame
# train = pd.DataFrame(data)
test = pd.DataFrame(data)

# Get data into object "Bunch" ----> Check if this is really needed!
# type(train)
type(test)

# Preparing the features matrix 
feature_cols = ['LeaseDuration']

# Need categorical features in numerical form
le = LabelEncoder()
test['LeaseDuration'] = le.fit_transform(test['LeaseDuration']) 

# Features matrix 
X_test = test[['LeaseDuration']]

# Response/target vector
y_test = test['Price']


# Modelling process

# Create linear regression object
lm = LinearRegression()

# Train model using the training data set
"""Use training data here """
fit = lm.fit(X_test, y_test)  

# The coefficients
print('Coef_: ', lm.coef_)
# The intercept
print('Coef_: ', lm.intercept_)

""" use testing data here"""
# The mean square error
print("Sum of squares: %.2f" % np.mean((lm.predict(X_test) - y_test) ** 2))
# Variance score - perfect is 1
print('Variance score: %.2f' % lm.score(X_test, y_test))

#Should return variance score 0 until you use the right data.. sake
