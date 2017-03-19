import array
import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pylab as plt
plt.use('Agg')

proteinFile = open('/home/lmt72/PDBbind2017/BabySet')
distances = []
a = []
for protein in proteinFile:
    protein = protein.strip()
    filename = "/home/lmt72/PDBbind2017/"+protein+".distances"
    distanceFile = open(filename)
    for line in distanceFile:
        data= line.split()
        secondProtein = data[0]
        distance = data[1].strip()
        distances.append(distance)
    a.append(distances)
    distances=[]
npArray = np.array(a)
Z1 = sch.linkage(npArray,method='average')
l1 = sch.leaves_list(Z1)
D = npArray[l1]
Z2 = sch.linkage(npArray.T,method='average')
l2 = sch.leaves_list(Z2)
D = D[:,l2]

fig = plt.figure(figsize=(8,8))
ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
z1 = hclust.dendrogram(Z1,orientation='left',labels=names[l1])
ax1.set_xticks([])
ax1.set_yticks([])

# Compute and plot second dendrogram.
ax2 = fig.add_axes([0.3,0.71,0.6,0.15])
z2 = hclust.dendrogram(Z2,labels=cells[l2])
ax2.set_xticks([])
ax2.set_yticks([])


# Plot distance matrix.
axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
im = axmatrix.matshow(D, aspect='auto', origin='lower')
    
axmatrix.set_xticks([])
axmatrix.set_xticks(range(len(cells)))
axmatrix.set_xticklabels(cells[l2],fontsize=2,rotation='vertical')
axmatrix.xaxis.set_tick_params(pad=95)
    
axmatrix.set_yticks(range(len(names)))
axmatrix.yaxis.tick_right()
axmatrix.set_yticklabels(names[l1],fontsize=5)

fig.subplots_adjust(bottom=0.1)
axcolor = fig.add_axes([0.3,0.07,0.6,0.02])
fig.colorbar(im,cax=axcolor,orientation='horizontal')
plt.savefig(sys.argv[3],dpi=600)
