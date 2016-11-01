import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib.font_manager
from scipy.io import *

def get_data(filename):
	X = np.loadtxt(filename)
	HOG = X[0: ,10:436]
	NaNs = np.isnan(HOG)
	HOG[NaNs] = 0
	return HOG

X_train = get_data('../../pets2015_ARENA_idt_bb/W1_ARENA-Rg_ENV_RGB_3.avi.txt')
print X_train

model = TSNE(n_components=2, random_state=0)
outp = model.fit_transform(np.array(X_train)) 

print "\n"

print outp
