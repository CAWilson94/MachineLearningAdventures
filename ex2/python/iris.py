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











