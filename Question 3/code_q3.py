import pandas as pd
import numpy as np

train_data = np.loadtxt('train_data.txt', skiprows=1)
train_data = pd.DataFrame(train_data)
train_data.columns = ['x1', 'x2', 'x3'] 

train_truth = np.loadtxt('train_truth.txt', skiprows=1)
train_truth = pd.DataFrame(train_truth)
train_truth.columns = ['y']

test_data = np.loadtxt('test_data.txt', skiprows=1)
test_data = pd.DataFrame(test_data)
test_data.columns = ['x1', 'x2', 'x3'] 

from sklearn.neural_network import MLPRegressor
fit = MLPRegressor(hidden_layer_sizes=(4,4,4,4))
print ("fitting model right now")
fit.fit(train_data,train_truth)
train_predicted = fit.predict(train_data)
test_predicted = fit.predict(test_data)

np.savetxt('test_predicted.txt', test_predicted, header='y', comments='')
