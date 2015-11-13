# CART = classification and regression trees
# Making splits that best separate the data for the 
# classes or predictions being made.

# Decision tree classifier
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from digit_example import predicted
print("hello")
print("iris example of CART");
# Load the iris datasets
dataset = datasets.load_iris();
# Fit a CART model to the dataset
model = DecisionTreeClassifier();
model.fit(dataset.data, dataset.target);
print(model);
#make predictions
expected = dataset.target;
predicted = model.predict(dataset.data);
#summarize the fit of the model
print(metrics.classification(expected,predicted));
print(metrics.confusion_matrix(expected,predicted));