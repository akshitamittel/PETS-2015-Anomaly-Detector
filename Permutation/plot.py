import sys
import numpy as np
import matplotlib.pyplot as plt 
from scipy.io import *
import os

# plt.figure()

# a = loadmat('hof_mbh_1/' + sys.argv[1])

# plt.plot(np.transpose(a['test1']),color='blue')
# plt.plot(np.transpose(a['test2']),color='red')
# plt.plot(np.transpose(a['train']),color='green')

# plt.show()

path = 'hog_hof_1/'   
dirs = os.listdir( path )

for fil in dirs:
	if fil.endswith("mat"):

		plt.figure()

		a = loadmat('hog_hof_1/' + fil)

		plt.plot(np.transpose(a['train']),color='green')
		plt.plot(np.transpose(a['test1']),color='blue')
		plt.plot(np.transpose(a['test2']),color='red')
		

		plt.savefig(fil[:len(fil)-4] + ".png")
		