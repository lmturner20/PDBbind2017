import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
from matplotlib import cm
import fastcluster as fcl
import glob
import os
import cPickle
import PIL

(npArray, D, Z1, names) = cPickle.load(open("clusterstate.pickle"))
im = PIL.Image.fromarray(cm.inferno(D,bytes=True))
im.save('heatmap.png')
