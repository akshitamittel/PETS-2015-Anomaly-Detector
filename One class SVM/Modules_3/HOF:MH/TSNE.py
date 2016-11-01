import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib.font_manager
from scipy.io import *

mat = loadmat("Threat1.mat")

m = mat["y_pred_test"]

model = TSNE(n_components=2, random_state=0)
outp = model.fit_transform(m)

print "\n"

print outp
