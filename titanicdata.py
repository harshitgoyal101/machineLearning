# -*- coding: utf-8 -*-
"""titanicData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JcKdI8nsrsSIKs8fe6jJWFE506j36uQ3
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib
import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf

dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') 
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') 

y_train = dftrain.pop('survived')
y_test = dfeval.pop('survived')

dftrain.head()
dftrain.age.hist(bins=10)

dftrain.sex.value_counts().plot(kind='bar')

dftrain['class'].value_counts().plot(kind='bar')

pd.concat([dftrain, y_train], axis=1).groupby('sex').survived.mean().plot(kind='bar').set_xlabel('% survive')