import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sklearn, argparse
import sklearn.metrics

parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('-g','--globe',type=str,required=True,help="Global file")
parser.add_argument('-l','--chain',type=str,required=True,help="Local file")
parser.add_argument('-r','--random',type=str,required=True,help="Random file")
parser.add_argument('-o','--outprefix',type=str,help="Prefix for output files, default <model>.<pid>",default='')
args = parser.parse_args()
globef = args.globe
chainf = args.chain
randomf = args.random
outprefix = args.outprefix

gtrue = []
gscore = []
globefile = open(globef,'r')
for line in globefile:
    if line.startswith('#'):
        pass
    else:
        data= line.split()
        gtrue.append( bool(float(data[0])) )
        gscore.append( float(data[1].strip()) )
fpr, tpr, _ = sklearn.metrics.roc_curve(gtrue,gscore)
auc = sklearn.metrics.roc_auc_score(gtrue,gscore)

ltrue = []
lscore = []
chainfile = open(chainf,'r')
for line in chainfile:
    if line.startswith('#'):
        pass
    else:
        data= line.split()
        ltrue.append( bool(float(data[0])) )
        lscore.append( float(data[1].strip()) )
fpr2, tpr2, _ = sklearn.metrics.roc_curve(ltrue,lscore)
auc2 = sklearn.metrics.roc_auc_score(ltrue,lscore)

rtrue = []
rscore = []
randomfile = open(randomf,'r')
for line in randomfile:
    if line.startswith('#'):
        pass
    else:
        data= line.split()
        rtrue.append( bool(float(data[0])) )
        rscore.append( float(data[1].strip()) )
fpr3, tpr3, _ = sklearn.metrics.roc_curve(rtrue,rscore)
auc3 = sklearn.metrics.roc_auc_score(rtrue,rscore)

fig = plt.figure(figsize=(8,8))
plt.plot(fpr,tpr,label='Global (AUC=%.4f)'%(auc),linewidth=12,color='b')
plt.plot(fpr2,tpr2,label='Local (AUC=%.4f)'%(auc2),linewidth=8,color='g')
plt.plot(fpr3,tpr3,label='Random (AUC=%.4f)'%(auc3),linewidth=4,color='r')
plt.legend(loc='lower right',fontsize=20)
plt.xlabel('False Positive Rate',fontsize=22)
plt.ylabel('True Positive Rate',fontsize=22)
plt.axes().set_aspect('equal')
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig('%s_roc.pdf'%outprefix,bbox_inches='tight')
