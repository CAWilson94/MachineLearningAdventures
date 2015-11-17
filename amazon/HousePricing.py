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
print "cols"
# Read in training & testing data
train_data = pd.read_csv(open('training_split.csv'), header=None, names=cols)
test_data = pd.read_csv(open('testing.csv'), header=None, names=cols)
print "read csv"
# Convert into pandas data frame
train = pd.DataFrame(train_data)
test = pd.DataFrame(test_data)
print "panda"
# Get data into object "Bunch" ----> Check if this is really needed!
type(train)
type(test)
print "bunches"
# Preparing the features matrix 
feature_cols = ['LeaseDuration']
print "transform"
# Need categorical features in numerical form
le = LabelEncoder()
train['LeaseDuration'] = le.fit_transform(train['LeaseDuration']) 
test['LeaseDuration'] = le.fit_transform(test['LeaseDuration']) 

# Features matrix 
X_train = train[['LeaseDuration']]
X_test = test[['LeaseDuration']]


# Response/target vector
y_train = train['Price']
y_test = test['Price']


# Modelling process

# Create linear regression object
lm = LinearRegression()

# Train model using the training data set
"""Use training data here """
fit = lm.fit(X_train, y_train)  

# The coefficients
print('Coef_: ', lm.coef_)
# The intercept
print('Coef_: ', lm.intercept_)

""" use testing data here"""
# The mean square error
print("Sum of squares: %.2f" % np.mean((lm.predict(X_test) - y_test) ** 2))
# Variance score - perfect is 1
print('Variance score: %.2f' % lm.score(X_test, y_test))


