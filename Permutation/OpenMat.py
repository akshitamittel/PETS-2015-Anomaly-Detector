from scipy.io import *
import numpy as np
import os
import errno
import sys 
import math

#Loading the three mat files
mat_dae = loadmat("results_dae/dae_50_pets3_hog_hof.mat")
mat_gmm = loadmat("results_gmm/gmm_pets3_hog_hof_5.mat")
mat_rbm = loadmat("results_rbm/grbm_30_pets3_hog_hof.mat")
print "loaded matrices from mat files."

#Scaling each array to a value between 0 and 1
def scale(min_val, max_val, val):
	return (val - min_val) / (max_val - min_val)

#Getting the three arrays stored in each mat file
def get_matrix(mat, power):
	test1 = []
	test2 = []
	train = []
	temp1 = []
	temp2 = []
	temp3 = []
	for i in mat["test1"][0]:
		if power != 0:
			i = math.exp(power*i)
		temp1.append(i)
	# print temp1
	# print min(temp1)
	# print max(temp1)
	for i in temp1:
		test1.append(scale(min(temp1), max(temp1), i))
	# print test1
	for i in mat["test2"][0]:
		if power != 0:
			i = math.exp(power*i)
		temp2.append(i)
	for i in temp2:
		test2.append(scale(min(temp2), max(temp2), i))
	for i in mat["train"][0]:
		if power != 0:
			i = math.exp(power*i)
		temp3.append(i)
	for i in temp3:
		train.append(scale(min(temp3), max(temp3), i))
	return test1, test2, train

dae_test1, dae_test2, dae_train = get_matrix(mat_dae, 0)
print "dae obtained"
gmm_test1, gmm_test2, gmm_train = get_matrix(mat_gmm, 1.0)
print "gmm obtained"
rbm_test1, rbm_test2, rbm_train = get_matrix(mat_rbm, -1.0)
print "rbm obtained"
print "All 9 arrays obtained"

for i in range(0,11):
	for j in range(0, i+1):

		list1 = []
		list2 = []
		list3 = []

		a = j * 0.1
		b = (i - j) * 0.1
		c = (10 - i) * 0.1

		length = min(np.size(dae_test1), np.size(gmm_test1), np.size(rbm_test1))
		print ("l", length)
		for k in range(0, length):
			x = (a * dae_test1[k]) + (b * gmm_test1[k]) + (c * rbm_test1[k])
			list1.append(x)

		length = min(np.size(dae_test2), np.size(gmm_test2), np.size(rbm_test2))
		for k in range(0, length):
			x = (a * dae_test2[k]) + (b * gmm_test2[k]) + (c * rbm_test2[k])
			list2.append(x)

		length = min(np.size(dae_train), np.size(gmm_train), np.size(rbm_train))
		print ("l", length)
		for k in range(0, length):
			x = (a * dae_train[k]) + (b * dae_test2[k]) + (c * dae_train[k])
			list3.append(x)

		np1 = np.asarray(list1)
		np2 = np.asarray(list2)
		np3 = np.asarray(list3)

		temp = {}
		temp["test1"] = np1
		temp["test2"] = np2
		temp["train"] = np3

		path = "hog_hof_1/"

		name = path + str(int(a*10)) + "_" +  str(int(b*10)) + "_" + str(int(c*10)) + ".mat"
		savemat(name, temp)

print "Permutation complete."