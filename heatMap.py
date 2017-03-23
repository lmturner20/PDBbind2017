import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
import fastcluster as fcl
import glob

#a = [12482][12842]
dict = {}
for (i,fname) in enumerate(glob.glob('*.distances')):
    pdb = fname.rstrip('.distances')
    dict[pdb] = i
length = len(dict)
print length
npArray = np.zeros((length,length))
    #filename = "/home/lmt72/PDBdistances/"+pdb+".distances"
for filename in glob.glob('/home/dkoes/PDBbind/general-set-with-refined/*/*_rec.pdb'):
    distanceFile = open(filename)
    for line in distanceFile:
        data= line.split()
        secondProtein = data[0]
        distance = float(data[1].strip())
        npArray[dict.get(pdb),dict.get(secondProtein)] = distance
        npArray[dict.get(secondProtein),dict.get(pdb)] = distance

#npArray = np.array(a)
Z1 = fcl.linkage(npArray,method='average')
l1 = sch.leaves_list(Z1)
D = (npArray[l1])
Z2 = fcl.linkage(npArray.T,method='average')
l2 = sch.leaves_list(Z2)
D = D[:,l2]

fig = plt.figure(figsize=(8,8))
ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
z1 = sch.dendrogram(Z1,orientation='left')
ax1.set_xticks([])
ax1.set_yticks([])

# Compute and plot second dendrogram.
ax2 = fig.add_axes([0.3,0.71,0.6,0.15])
z2 = sch.dendrogram(Z2)
ax2.set_xticks([])
ax2.set_yticks([])

# Plot distance matrix.
axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
im = plt.matshow(D, aspect='auto', origin='lower')

fig.subplots_adjust(bottom=0.1)
axcolor = fig.add_axes([0.3,0.07,0.6,0.02])
fig.colorbar(im,cax=axcolor,orientation='horizontal')
plt.savefig('heatmap',dpi=600)
