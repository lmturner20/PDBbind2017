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

index = dict()
for (i,fname) in enumerate(glob.glob('/home/lmt72/PDBdistances/*.distances')):
    fname = os.path.basename(fname)
    if fname.endswith('.distances'):
        pdb = fname[:-10]
        index[pdb] = i
length = len(index)
print length
npArray = np.zeros((length,length))
for filename in glob.glob('/home/lmt72/PDBdistances/*.distances'):
    distanceFile = open(filename)
    for line in distanceFile:
        data= line.split()
        secondProtein = data[0]
        distance = float(data[1].strip())
        i = index[pdb]
        npArray[i,index[secondProtein]] = distance
        npArray[index[secondProtein],i] = distance
names = ['' for x in xrange(length)]
for (name,i) in index.iteritems():
    names[i] = name

Z1 = fcl.linkage(npArray,method='average')
l1 = sch.leaves_list(Z1)
D = (npArray[l1])
Z2 = fcl.linkage(npArray.T,method='average')
l2 = sch.leaves_list(Z2)
D = D[:,l2]
cPickle.dump((npArray,D, Z1, names),open("clusterstate.pickle",'w'),-1)

(npArray, D, Z1, names) = cPickle.load(open("clusterstate.pickle"))
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
ax1.set_xticks([])
ax1.set_yticks([])

# Compute and plot second dendrogram.
ax2 = fig.add_axes([0.3,0.71,0.6,0.15])
ax2.set_xticks([])
ax2.set_yticks([])

# Plot distance matrix.
axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
im = PIL.Image.fromarray(cm.gist_earth(D,bytes=True))

fig.subplots_adjust(bottom=0.1)
axcolor = fig.add_axes([0.3,0.07,0.6,0.02])
fig.colorbar(im,cax=axcolor,orientation='horizontal')
im.savefig('heatmap',dpi=600)
