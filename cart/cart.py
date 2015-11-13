# CART = classification and regression trees
# Making splits that best separate the data for the 
# classes or predictions being made.

# Decision Tree Classifier
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

# load the iris datasets
dataset = datasets.load_iris()
# fit a CART model to the data
model = DecisionTreeClassifier()
model.fit(dataset.data, dataset.target)
print(model)
# make predictions
expected = dataset.target
predicted = model.predict(dataset.data)
# summarize the fit of the model
print("\nclass report\n")
print(metrics.classification_report(expected, predicted))
print("\nconfusion matrix\n")
print(metrics.confusion_matrix(expected, predicted))