# The task here is to predict, given an image, what digit it represents
# Given samples of each of the ten classes (digits 0-9)
# We fit an ESTIMATOR on each of these, which is able to predict 
# the classes to which unseen samples belong

# In scikit-learn: an estimator for classification is a python object that implements the method fit(x,y) and predict(T)
# Estimator for classification --> python object implementing fit(x,y) and predict(T)

#sklearn.svm.SVC is an estimator class that implements support vector classification 

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100);



