# Charlotte Wilson
# SciKit learn example
# How starting from the original problem data
# can shaped for consumption in scikit-learn.


# importing a dataset
from sklearn import datasets
# data member is an n_sample and n_features array
iris = datasets.load_iris();
digits = datasets.load_digits();

# digits.data accesses the features that can be used to classify the digit samples
# data --> features
# These features each belong to a class
print(iris.data);
print("\n");
print(digits.data);

# digits.target gives ground truth for the data set
# i.e. the number corresponding to each digit we are trying to learn    
# target --> class
print("digits target yo!");
print(digits.target);

# Shape of the data arrays
# The data is always a 2d array
# shape(n_samples,n_features)
# Although the original data may have a different shape.
# Each original sample in an image of shape (8,8) can 
# be accessed using:
print("\nShape of data arrays \n");
print(digits.images[0]);



###########LEARNING AND PREDICTING#########################

# The task here is to predict, given an image, what digit it represents
# Given samples of each of the ten classes (digits 0-9)
# We fit an ESTIMATOR on each of these, which is able to predict 
# the classes to which unseen samples belong

# In scikit-learn: an estimator for classification is a python object that implements the method fit(x,y) and predict(T)
# Estimator for classification --> python object implementing fit(x,y) and predict(T)

# sklearn.svm.SVC is an estimator class that implements support vector classification 
# Consider the estimator as a black box for now
from sklearn import svm

# Choosing the paramaters for the model:
# In this case we have selected the value of gamma manually 
# Possible to select good values automatically using tools 
# Tools for auto selection: grid search, cross validation

# Call our estimator clf, since it is a classifier
# Must now be fitted to the model
# i.e. it must learn from the model
clf = svm.SVC(gamma=0.001, C=100);

# We pas our training set to fit the method
# So we use all images in our dataset bar the last one, as a training set.

# We select this training set with the [:-1] python syntax,
# which produces a new array that contains all but the last entry of digits.data
something = clf.fit(digits.data[:-1], digits.target[:-1]);
print("\nclassifier shit...\n");

print(something);


array = clf.predict(digits.data[:-1])

(array[8]);








