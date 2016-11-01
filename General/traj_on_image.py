import cv2
import numpy as np
from scipy.io import *
import os
import matplotlib.pyplot as plt
j = 1;
prefix1 = 'hof_mbh/hof_mbh_grbm_30/hof_mbh_1/'
test_feat = np.loadtxt('A1_ARENA-Tt_ENV_RGB_3.avi.txt')
a = loadmat(prefix1 + '1_2_7.mat')
y_pred_test = a['test1']
test_feat_new = test_feat[np.all(y_pred_test<800,axis=0),0:]
#os.mkdir(prefix)
in_vid = cv2.VideoCapture('A1_ARENA-Tt_ENV_RGB_3.avi')
#out_vid = cv2.VideoWriter.open(prefix+'A1_ARENA-Tt_ENV_RGB_3_traj.avi') 
i = 1 
j = 0
while(True):
    ret, frame = in_vid.read()
    plt.imshow(frame)
    #plt.show()
    plt.hold(True)
    while j<test_feat_new.shape[0]:
        if test_feat[j,0]==i:
            plt.scatter(np.round(test_feat_new[j,1]),np.round(test_feat_new[j,2]))
            plt.hold(True)
            j = j+1
        else:
            break
    #plt.show()
    plt.savefig(str(i)+'.jpg')
    plt.close()
    im = cv2.imread(str(i)+'.jpg');
    #out_vid.write(im)
    i = i+1
#out_vid.close()