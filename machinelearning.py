# -*- coding: utf-8 -*-
"""machineLearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Lh-U80OTMSkqVzJF-uZeklfWATZYZfD

Machine Learning
"""

from scipy.spatial import distance

class Dodo:
  
  #memorization
  def fit(self,X_train,y_train):
    self.X_train = X_train
    self.y_train = y_train
  
  #ans of our Ml
  def predict(self,X_test):
    predictions = []
    for row in X_test:
      label = self.closest(row)
      predictions.append(label)
    return predictions

  #finding closest element
  def closest(self,row):
    best_dist = distance.euclidean(row,self.X_train[0])
    best_idx = 0
    for i in range(1,len(self.X_train)):
      dist = distance.euclidean(row,self.X_train[i])
      if dist < best_dist:
        best_dist = dist
        best_idx = i
    return self.y_train[best_idx]

#load dataset
from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

#Dividing dataset
from sklearn.model_selection import train_test_split
X_train ,X_test, y_train, y_test = train_test_split(X,y,test_size=0.5)

#Object of dataset
clf = Dodo()

#training ML
clf.fit(X_train,y_train)
#ML predications
y_ans = clf.predict(X_test)

#accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_ans))

"""Visualizing a Tree"""

from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())