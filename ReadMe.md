#PETS 2015 challenge: Anomaly detection on the ARENA Dataset

The challenge and the dataset can be found at: http://www.cvg.reading.ac.uk/PETS2015/

##This folder consists of 3 sub directories as follows:

## 1. General
=============
The code traj_on_image.py is used to plot back the results from various models onto the test video’s, according to the threshold that we chose.



## 2. Permuatation:
======================

This section consists of codes and output (we selected 2  for demonstration purposes) related to the Genetic Algorithm approach.

The nomenclature of various .mat and .jpg files in this directory are as follows:
	a_b_c
	where “a”, “b”, “c” are the coefficients of the scores obtained from autoencoders, GMM’s, and RBM’s respectively.

1. hof_mbh_1: It consists of scores which are a different combinations of GMM, RBM, and auto encoders for combinations of HOF and MBH.
T1 and T2: Consist of all the frames after the “anomalous” points are plotted back onto the video.

2. hog_hof_1:It consists of scores which are a different combinations of GMM, RBM, and auto encoders for combinations of HOF and HOG.
T1: Consist of all the frames after the “anomalous” points are plotted back onto the video.

3. OpenMat.py: This is the source code, that takes as an input the mat files which contain the scores obtained from Autoencoders, GMM’s, and RBM’s. The code extracts the value’s and applies different permutations of coefficients and stores the results in mat files. 
		You have to modify the value’s in the load mat functions to the path where your input scores are.

4. plot.py: This is a general source code that plots the scores obtained from OpenMat.py onto graphs.
		Like OpenMat.py you have to modify the value of the variable path to indicate where your mat files are.



##One class SVM:
===============
This section contains the different feature extractions for on view of our data-set.

	1. Modules_3: This consists a list of all the different combinations of the features that were extracted. The names of the subdirectories indicate the combination of features.
	Here the warning video in the data-set was used as the training data-set. Each file consist of a small code which trains the given SVM. The mat files generated hold the SVM results for both test videos.
 
	2. Results: This showcases some of the examples of the output that was generated from the One-class SVM’s after mapping the points back onto the test-cases given in the data-set.