import pandas as pd
import numpy as np
from skimage.measure import label
#the version of skimage should be 0.15.0

input_question_4=np.loadtxt('input_question_4', dtype=int)
output_question_4_connectivity4=label(input_question_4,connectivity=1)
np.savetxt('output_question_4_connectivity4.txt', output_question_4_connectivity4,fmt='%d')
output_question_4_connectivity8=label(input_question_4,connectivity=2)
np.savetxt('output_question_4_connectivity8.txt', output_question_4_connectivity8,fmt='%d')
