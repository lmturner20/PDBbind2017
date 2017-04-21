import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sklearn, argparse
import sklearn.metrics

parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('-g','--globe',type=str,required=True,help="Global file")
parser.add_argument('-l','--chain',type=str,required=True,help="Local file")
parser.add_argument('-r','--random',type=str,required=True,help="Random file")
args = parser.parse_args()
globef = args.globe
chainf = args.chain
randomf = args.random

gtrue = []
gscore = []
globefile = open(globef,'r')
for line in globefile:
    data= line.split()
    gtrue.append( bool(data[0]) )
    gscore.append( data[1].strip() )
fpr, tpr, _ = sklearn.metrics.roc_curve(gtrue,gscore)
auc = sklearn.metrics.roc_auc_score(gtrue,gscore)

ltrue = []
lscore = []
chainfile = open(chainf,'r')
for line in chainfile:
    data= line.split()
    ltrue += data[0]
    lscore += float(data[1].strip())
fpr2, tpr2, _ = sklearn.metrics.roc_curve(ltrue,lscore)
auc2 = sklearn.metrics.roc_auc_score(ltrue,lscore)

rtrue = []
rscore = []
randomfile = open(randomf,'r')
for line in randomfile:
    data= line.split()
    rtrue += data[0]
    rscore += float(data[1].strip())
fpr3, tpr3, _ = sklearn.metrics.roc_curve(rtrue,rscore)
auc3 = sklearn.metrics.roc_auc_score(rtrue,rscore)

fig = plt.figure(figsize=(8,8))
plt.plot(fpr,tpr,label='CNN (AUC=%.2f)'%(auc),linewidth=4,color=b)
plt.plot(fpr2,tpr2,label='CNN (AUC=%.2f)'%(auc2),linewidth=4,color=g)
plt.plot(fpr3,tpr3,label='CNN (AUC=%.2f)'%(auc3),linewidth=4,color=r)
plt.legend(loc='lower right',fontsize=20)
plt.xlabel('False Positive Rate',fontsize=22)
plt.ylabel('True Positive Rate',fontsize=22)
plt.axes().set_aspect('equal')
plt.tick_params(axis='both', which='major', labelsize=16)
plt.text(.05, -.25, txt, fontsize=22)
plt.savefig('%s_roc.pdf'%outprefix,bbox_inches='tight')
