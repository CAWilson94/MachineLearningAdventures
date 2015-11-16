#import numpy as np
#data = np.loadtxt('Advertising.csv', delimiter=',')

""" 
import pandas as pd
data = pd.read_csv(open('myfile.csv'))
target = data[target_column_name]
del data[target_column_name]

# Then fit a scikit-learn estimator
SVC().fit(data, target)
"""
#Import the data
import pandas as pd
data = pd.read_csv(open('pp-complete.csv'))

#Bunch the data!!
type(data)
# Get the features and samples matrix from it
feature_cols = data.columns
X = data[feature_cols]
# Get the target/response vector from it
y = data.Sales

print "column header defaults?"
print data.columns

#target is column 2
"""index_col = data.columns[3]
print index_col
target = index_col
print target
"""
