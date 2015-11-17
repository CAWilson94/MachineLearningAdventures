'''
Created on 16 Nov 2015
@author: charlotto
'''
import pandas as pd
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


# Column headers to make things a bit easier later on
cols = ['ID', 'Price', 'Date', '4', 'PropType', '6', 'LeaseDuration',
        '8', '9', '10', '11', 'Location', '13', '14', '15', '16']

# Read in training data
data = pd.read_csv(open('testing.csv'), header=None, names=cols)
# Read in testing data 
# data = pd.read_csv(open('testing.csv'), header=None, names=cols)

# Convert into pandas data frame
test = pd.DataFrame(data)
# train = pd.DataFrame(data)
# Get data into object "Bunch"
type(test)
# type(test)

feature_cols = ['LeaseDuration']

X_test = test[feature_cols]
# X_train = train[features_cols]

# label encoder, fit and transform
# X = le.fit_transform(pData[feature_cols])  
# X = pData['LeaseDuration'].apply(lambda lD: 0 if lD == "F" else 1) 
print X_test.shape
# Response/target vector
y_test = test['Price']
# y_train = train['Price']
# print y

# Modelling process now!
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
# lm.fit(X, y)
# print "got here"
# predict = lm.predict(X)

# metrics.accuracy_score(y_test,y_predict)
# plot_confusion_matrix(y_test, y_predict)





