import pandas as pd
import numpy as np

### (1) Write a code to convert given coordinates to index
input_coordinates_7_2 = np.loadtxt('input_coordinates_7_2.txt', skiprows=1, dtype=int)
input_coordinates_7_2 = pd.DataFrame(input_coordinates_7_2)
input_coordinates_7_2.columns = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']

def CoordinatesToIndex(coordinates,l,d):
    indexes=[]
    for k in range(len(coordinates)):
        index=0
        for i in range(1,d+1):
            ls=1
            for j in range(1,i):
                ls=ls*l[j-1]
            index=index+coordinates['x'+str(i)][k]*ls
        indexes.append(index)
    coordinates['index']=indexes
    return coordinates

l=[4, 8, 5, 9, 6, 7]
d=6
input_coordinates_7_2=CoordinatesToIndex(input_coordinates_7_2,l,d)
np.savetxt('output_index_7_2.txt', input_coordinates_7_2['index'], header='index', comments='',fmt='%d')

### (2) Write a code to convert given index to coordinates
input_index_7_2 = np.loadtxt('input_index_7_2.txt', skiprows=1, dtype=int)
input_index_7_2 = pd.DataFrame(input_index_7_2)
input_index_7_2.columns = ['index']

def IndexToCoordinates(index,l,d):
    #use the recursive method
    coordinates=[]
    if (d==1):
        coordinates=[index%l[0]]
    else:
        ls=1
        for i in range(1,d):
            ls=ls*l[i-1]
        coordinates.extend(IndexToCoordinates(index%ls,l,d-1))
        coordinates.append(index//ls)
    return coordinates

l=[4, 8, 5, 9, 6, 7]
d=6
output_coordinates_7_2=[]
for i in range(len(input_index_7_2)):
    output_coordinates_7_2.append(IndexToCoordinates(input_index_7_2['index'][i],l,d))
output_coordinates_7_2=np.array(output_coordinates_7_2)
np.savetxt('output_coordinates_7_2.txt', output_coordinates_7_2, header='x1 x2 x3 x4 x5 x6', comments='',fmt='%-2d')



