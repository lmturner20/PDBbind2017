import array
import numpy as np
import scipy.cluster.hierarchy as sch

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
Z1 = hclust.linkage(npArray,method='average')
l1 = hclust.leaves_list(Z1)
D = npArray[l1]
Z2 = hclust.linkage(npArray.T,method='average')
l2 = hclust.leaves_list(Z2)
D = D[:,l2]
