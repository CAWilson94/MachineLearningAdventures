# import iris function from datasets Module
# convention is to import classes, modules or functions
# as opposed to importing scikit learn as a whole
from sklearn.datasets import load_iris
# save return value in an object called iris
# this object is a container called a "bunch" 
# which is scikit learns data type for storing 
# datasets and their attributes
iris = load_iris();
# type(iris) --> Do you really need this?
# Each row represents one flower, 
# print the iris data
# each collumn represents the four measurments
type(iris);
print "iris.data"
print (iris.data);
"""
Example start of dataset output 
[[ 5.1  3.5  1.4  0.2]
 [ 4.9  3.   1.4  0.2]
 [ 4.7  3.2  1.3  0.2]
 [ 4.6  3.1  1.5  0.2]
 [ 5.   3.6  1.4  0.2]
 """
# Each row is known as an OBSERVATION
# Other terms are sample, example, instance and record

# Thus, the iris data set has 150 observations! :D
    
# Each collumn is known as a FEATURE! 
# Some other terms are: attribute, indepenant variable, input,
# regressor and covariant.

# Thus the iris dataset has 4 features! :D

# print the names of the 4 features
print(iris.feature_names);
# Print integer representing the species of each Observation
print(iris.target);
print(iris.target_names);
# The target represnts what we are going to predict
# other terms for target: response, outcome, label and dependant variable
# 0 - setosa 
# 1 - veriscolor
# 2 - virginica


# Types of problems:
####################
# CLASSIFICATION --> the target or response being predicted is categorical! 
# meaning that its values are in a finite unordered set

# REGRESSION --> The response or target is ordered and continuous. Such as a price of a house
# THIS IS THE ONE YOU WANT!

# For this data set, the iris data set
# How can we tell this is classification and not regression?
# You need to understand how the date is encoded first 
# Then decide if the response variable is suitable for 
# regression or classification

# The 0 1 and 2 represent unordered categories ...
# 9:15

# Requirements for working with scikit learn:
############################################
# 1. Features and response - Separate objects
# 2. Features and response - Numeric
# 3. Features and response - NumPy arrays
# 4. Features and response - Specific shapes
############################################

# Need to first learn the relationship between the features and the response
# But first we should make sure the features and response are in the form 
# that scikit learn expects! (details above).

# Check type of features and response
# Since iris.data and iris.target are stored separatly 
# They fulfill the first condition.
# check NumPy arrays!
print type(iris.data)
print type(iris.target)
# Check shape of features
# first dimension = number of observation
# second dimension = number of features
# output: (150L,4L) as expected
print(iris.data.shape);
# Check shape of response
# single dimension matching number of observations
# output: (150L,) as expected
######################################### There should be one response corresponding to each observation ###################
print(iris.target.shape);

# The scikit learn convention is for the feature data to be stored in an object named x
# And for the response data to be stored in an object named y
# Store  feature matrix in "x" : X capitalised because it represents a matrix
X = iris.data
# Store response vector in "y" : lower case because it represents a vector
y = iris.target

######################################## TRAINING THE LEARNING MODEL YOOOOOO ###############################################
"""
How would we, as humans look at the data and tell the difference between 
the species?

Well, if you look at the data, each speciec of flower seem to have similar 
measurements.

When looking for unknown iris we will look at iris with similar measurements
and assume they are the same species of unknown iris.

######################################### K Nearest Neighbour Classification (KNN) #########################################

Steps in K nearest neighbour:
1. Pick a value K
2. Search for K observations in training data that are "nearest" to measurements of unknown iris.

     More on how to pick the k later...
   
     So say we pick 5 as our K:
     The model calculates the numerical distance between the unknown iris and each of the 150 known iris's
     and selects the 5 known iris's with the smallest distance to the unknown iris.
     
3. Use most popular response value from the K nearest neighbours as predicted response value for 
   the unknown iris.
   Popular response value --> predicted response value for unknown iris.
   
   What does it mean by most popular?  

"""

""" ------------------------------- Scikit learn 4 step modelling pattern ----------------------------------------------------"""
# 1. import the class you plan to use
from sklearn.neighbors import KNeighborsClassifier

# 2. Instantiate the Estimator (model) so called due 
# to their primary goal being to estimate unknown quantities.
# Creating an instance of the KNeighborsClassifier class!
knn = KNeighborsClassifier(n_neighbors=5);

# We now have an object called knn that knows how to do
# K nearest neighbours classification!
# It is now just waiting for us to give it some data. 
print(knn);

# 3. Fit the model with data - MODEL TRAINING!
# Model is learning the relationship between X and y 
# Occurs in-place so dont need to assign it to an object
knn.fit(X, y);

# 4. predict the response of the new observation
# New observations called "out of sample" data
# Uses the information it learned during the model training process.

# Inputting measurements for unknown iris, and asking fitted model
# to predict the iris species based on what it has learned in the previous step.

array = knn.predict([3, 5, 4, 2])  # WARNING HOW TO FIX?
print array
# Can use predict on multiple observations at once
# 2 by 4 : 2 observations with 4 features each
X_new = [[3, 5, 4, 2], [5, 4, 3, 2]]
print knn.predict(X_new);

# Using a different value for K
################################
# So if you changed from k=1 to 5 this is known as model tuning
# you are varying the arguments that you pass to the model!! 

# Using a different classification model
########################################
# Because the models all have the same interface,
# we can use the same 4 step pattern on them all.

# Lets give logistic regression a go!

#import the class 
from sklearn.linear_model import LogisticRegression

print("\nlogreg!\n");
#instantiate the model (using default parameters)
logreg = LogisticRegression();  

#Fit the model with data
logreg.fit(X, y)

#Predict response for new observations
print logreg.predict(X_new)





