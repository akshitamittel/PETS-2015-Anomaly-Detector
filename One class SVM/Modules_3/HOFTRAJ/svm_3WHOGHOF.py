'''
Training set contains only warning. 
PETs camera 3.
Only TRAJ and HOF features are extracted.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from sklearn import svm
from scipy.io import *

#Extracting the HOG features
def get_data(filename):
	X = np.loadtxt(filename)
	TRAJ = X[0: ,10:40]
	NaNs = np.isnan(TRAJ)
	TRAJ[NaNs] = 0
	HOF = X[0: ,136:244]
	NaNs = np.isnan(HOF)
	HOF[NaNs] = 0
	return np.hstack((TRAJ , HOF))

#creating the single class SVM
clf = svm.OneClassSVM(nu = 0.01, kernel = "rbf")

#Training your SVM
X_train = get_data('../../pets2015_ARENA_idt_bb/W1_ARENA-Rg_ENV_RGB_3.avi.txt')
clf.fit(X_train)

#Generating the test result
X_test = get_data('../../pets2015_ARENA_idt_bb/A1_ARENA-Tt_ENV_RGB_3.avi.txt')
y_pred_test = clf.predict(X_test)
print "Test 1"
savemat("Threat1.mat", {'y_pred_test': y_pred_test})

X_test = get_data('../../pets2015_ARENA_idt_bb/A2_ARENA-Tt_ENV_RGB_3.avi.txt')
y_pred_test = clf.predict(X_test)
print "Test 2"
savemat("Threat2.mat", {'y_pred_test': y_pred_test})
