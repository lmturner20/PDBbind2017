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
np.set_printoptions(threshold=np.inf,precision=2)
print npArray
npArray = sch.average(npArray)
print npArray
npArray = sch.leaves_list(npArray)
print npArray
