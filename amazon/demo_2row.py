# from sklearn.datasets.base import load_files
# s1 = load_files()

# imports
import pandas as pd
import matplotlib.pyplot as plt
from patsy.desc import INTERCEPT
from sklearn.preprocessing.label import LabelEncoder
from sklearn import preprocessing

print "read in csv"
# Read data into a data frame
data = pd.read_csv('Advertising.csv', index_col=0);
print "now to get shape of data..."
print data.head()

# print data.shape
print data.shape
# data.shape prints (n_samples,N_features)
# where n starts from 0, so  we have 3 rows which should show as 2

#create X and y:
feature_cols = ['TV','Radio','Newspaper']


X= data[feature_cols]
print X.shape
y= data.Sales
print "printing y"
print y
# follow the usual sklearn pattern: import, instantiate, fit

#import
from sklearn.linear_model import LinearRegression
#instantiate
lm = LinearRegression()
#fit
lm.fit(X, y)

#print intercept and coefficients 
print lm.intercept_
print lm.coef_

#pair feature names with coefficients
print zip(feature_cols, lm.coef_)
#predict for new observation
print lm.predict([100, 25, 25])
#calculate the R squared 
print lm.score(X, y)
