import pandas as pd
import numpy as np

### (1) Write a code to convert given coordinates to index
input_coordinates_7_1 = np.loadtxt('input_coordinates_7_1.txt', skiprows=1, dtype=int)
input_coordinates_7_1 = pd.DataFrame(input_coordinates_7_1)
input_coordinates_7_1.columns = ['x1', 'x2']

def CoordinatesToIndex(coordinates,l1,l2):
    coordinates['index']=coordinates['x2']*l1+coordinates['x1']
    return coordinates

input_coordinates_7_1=CoordinatesToIndex(input_coordinates_7_1,50,57)
np.savetxt('output_index_7_1.txt', input_coordinates_7_1['index'], header='index', comments='',fmt='%d')

### (2) Write a code to convert given index to coordinates
input_index_7_1 = np.loadtxt('input_index_7_1.txt', skiprows=1, dtype=int)
input_index_7_1 = pd.DataFrame(input_index_7_1)
input_index_7_1.columns = ['index']

def IndexToCoordinates(index,l1,l2):
    index['x1']=index['index']%l1
    index['x2']=index['index']//l1
    return index

input_index_7_1=IndexToCoordinates(input_index_7_1,50,57)
np.savetxt('output_coordinates_7_1.txt', input_index_7_1[['x1','x2']], header='x1 x2', comments='',fmt='%d')
