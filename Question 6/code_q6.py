import pandas as pd
import numpy as np

input_question_6_polygon = np.loadtxt('input_question_6_polygon', dtype=int)
input_question_6_points = np.loadtxt('input_question_6_points', dtype=int)


def isRayIntersectsSegment(poi,s_poi,e_poi): 
    #input：point，edge start point，edge end point
    if s_poi[1]==e_poi[1]: #the line segment is parallel or coincident with the ray
        return False
    if s_poi[1]>poi[1] and e_poi[1]>poi[1]: #the line segment is above the ray
        return False
    if s_poi[1]<poi[1] and e_poi[1]<poi[1]: #the line segment is below the ray
        return False
    if s_poi[1]==poi[1] and e_poi[1]>poi[1]: #the intersection is the lower endpoint (spoint)
        return False
    if e_poi[1]==poi[1] and s_poi[1]>poi[1]: #the intersection is the lower endpoint (epoint)
        return False
    if s_poi[0]<poi[0] and e_poi[1]<poi[1]: #the line segment is to the left of the ray
        return False

    xseg=e_poi[0]-(e_poi[0]-s_poi[0])*(e_poi[1]-poi[1])/(e_poi[1]-s_poi[1]) #calculate the intersection
    if xseg<poi[0]: #the intersection is to the left of the beginning of the ray (point)
        return False
    return True  

def isPoiWithinPoly(poi,poly):
    #input：point，polygon
    sinsc=0 #the number of intersections
    for i in range(len(poly)-1): #[0,len-1]
        s_poi=poly[i]
        e_poi=poly[i+1]
        if isRayIntersectsSegment(poi,s_poi,e_poi):
            sinsc+=1 
    return True if sinsc%2==1 else False

f=open('output_question_6','a')
for i in range(len(input_question_6_points)):
    status='inside' if (isPoiWithinPoly(input_question_6_points[i],input_question_6_polygon)) else 'outside'   
    f.write(str(input_question_6_points[i][0])+' '+str(input_question_6_points[i][1])+' '+status+'\n')
f.close()
