import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

# for attr in dir(iris):
#     print(attr)

feature_names = iris.feature_names
n_feature = len(feature_names)
species = iris.target_names
n_species = len(species)

iris_X, iris_y = iris.data, iris.target