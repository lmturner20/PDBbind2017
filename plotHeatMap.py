import numpy
import cPickle
import PIL
from matplotlib import cm

(npArray, D, Z1, names) = cPickle.load(open("clusterstate.pickle"))
im = PIL.Image.fromarray(cm.gist_earth(D,bytes=True))
im.save('heatmap.png')
