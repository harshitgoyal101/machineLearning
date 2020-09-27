# -*- coding: utf-8 -*-
"""Titanic2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hQHcEpytec8Erelc1LzHg85HWLckrtc9
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib
import tensorflow as tf
import tensorflow.compat.v2.feature_column as fc
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

CC = ['sex','n_siblings_spouses','parch','class','deck','embark_town','alone']
NC = ['age','fare']

features_columns = []
for feature_name in CC:
  vocabulary = dftrain[feature_name].unique()
  features_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name,vocabulary))

for feature_name in NC:
  features_columns.append(tf.feature_column.numeric_column(feature_name))

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):

  def input_function():
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
    if shuffle:
      ds = ds.shuffle(1000)
    ds = ds.batch(batch_size).repeat(num_epochs)
    return ds

  return input_function


train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn  = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

linear_est = tf.estimator.LinearClassifier(feature_columns=features_columns)
linear_est.train(train_input_fn)

result = linear_est.evaluate(eval_input_fn)
clear_output()
print(result['accuracy'])

result = list(linear_est.predict(eval_input_fn))
clear_output()
print(dfeval.loc[5])
print(result[5]['probabilities'][1])