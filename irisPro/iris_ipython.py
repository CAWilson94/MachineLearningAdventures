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
# each collumn represents the four measurments
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
#Print integer representing the species of each Observation
print(iris.target);