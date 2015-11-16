# import numpy as np
# data = np.loadtxt('Advertising.csv', delimiter=',')

""" 
import pandas as pd
data = pd.read_csv(open('myfile.csv'))
target = data[target_column_name]
del data[target_column_name]

# Then fit a scikit-learn estimator
SVC().fit(data, target)
"""
# Import the data
import pandas as pd
data = pd.read_csv(open('pp-complete.csv'))

# Bunch the data!!
type(data)
# Get the features and samples matrix from it
feature_cols = data.columns
"""
Will need to use data.columns to get the 
default column headers then allocate the 
features_cols to those specific columns 
as shown in demo_2row.

i.e. if the default columns are say, 
London, Sales, PropType...
you want to have the following:
feature_cols =['London','PropType']
and then have your response vector as:
y = data.Sales since the sales price is our
target, what we want to predict.

"""
X = data[feature_cols]
# Get the target/response vector from it
y = data.Sales

print "column header defaults?"
print data.columns

# target is column 2
"""index_col = data.columns[3]
print index_col
target = index_col
print target
"""
##################### Modelling process #############

# 1. Import model
# 2. Instantiate model
# 3. Fit model with data (train)
# 4. Predict response for new observations

"""
The above is training the data, so now we want to test
the data, see if our predictions match up and evaluate 
the model we have created. 
"""
