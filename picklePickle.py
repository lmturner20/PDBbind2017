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

parser.add_argument('-d','--directory',type=str,required=False,help="Directory with distance files")
args = parser.parse_args()

index = dict()
for (i,fname) in enumerate(glob.glob(args.directory+'/*.distances')):
    fname = os.path.basename(fname)
    if fname.endswith('.distances'):
        pdb = fname[:-10]
        index[pdb] = i
length = len(index)
npArray = np.zeros((length,length))
for filename in glob.glob(args.directory+'/*.distances'):
    distanceFile = open(filename)
    filename = os.path.basename(filename)
    if filename.endswith('.distances'):
        pdb = filename[:-10]
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
print npArray

Z1 = fcl.linkage(npArray,method='average')
l1 = sch.leaves_list(Z1)
D = (npArray[l1])
Z2 = fcl.linkage(npArray.T,method='average')
l2 = sch.leaves_list(Z2)
D = D[:,l2]
cPickle.dump((npArray,D, Z1, names),open("clusterstate.pickle",'w'),-1)
