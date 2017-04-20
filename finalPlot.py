import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sklearn
import sklearn.metrics

parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('-g','--globe',type=str,required=True,help="Global pid")
parser.add_argument('-l','--chain',type=str,required=True,help="Local pid")
parser.add_argument('-r','--random',type=str,required=True,help="Random pid")
args = parser.parse_args()

globepid = args.globe
globef = open('/net/pulsar/koes/lmt72/PDBbind/global.finaltest,'a')
globe0 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+globepid+'.0.finaltest','r')
for line in globe0
    globef.write(line)
globe0.close()
globe1 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+globepid+'.1.finaltest','r')
for line in globe1
    globef.write(line)
globe1.close()
globe2 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+globepid+'.2.finaltest','r')
for line in globe2
    globef.write(line)
globe2.close()
globef.close()

chainpid = args.chain
chainf = open('/net/pulsar/koes/lmt72/PDBbind/local.finaltest,'a')
chain0 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+chainpid+'.0.finaltest','r')
for line in chain0
    chainf.write(line)
chain0.close()
chain1 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+chainpid+'.1.finaltest','r')
for line in chain1
    chainf.write(line)
chain1.close()
chain2 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+chainpid+'.2.finaltest','r')
for line in chain2
    chainf.write(line)
chain2.close()
chainf.close()

randompid = args.random
randomf = open('/net/pulsar/koes/lmt72/PDBbind/random.finaltest,'a')
random0 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+randompid+'.0.finaltest','r')
for line in random0
    randomf.write(line)
random0.close()
random1 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+randompid+'.1.finaltest','r')
for line in random1
    randomf.write(line)
random1.close()
random2 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+randompid+'.2.finaltest','r')
for line in random2
    randomf.write(line)
random2.close()
randomf.close()

ytrue = []
#load in ytrue
yscore = []
#load in yscore
fpr, tpr, _ = sklearn.metrics.roc_curve(ytrue,yscore)
auc = sklearn.metrics.roc_auc_score(ytrue,yscore)

ytrue2 = []
#load in ytrue
yscore2 = []
#load in yscore
auc2 = sklearn.metrics.roc_auc_score(ytrue,yscore)

ytrue3 = []
#load in ytrue
yscore3 = []
#load in yscore
auc3 = sklearn.metrics.roc_auc_score(ytrue,yscore)

fig = plt.figure(figsize=(8,8))
plt.plot(fpr,tpr,label='CNN (AUC=%.2f)'%(auc),linewidth=4)
plt.plot(fpr,tpr,label='CNN (AUC=%.2f)'%(auc2),linewidth=4)
plt.plot(fpr,tpr,label='CNN (AUC=%.2f)'%(auc3),linewidth=4)
plt.legend(loc='lower right',fontsize=20)
plt.xlabel('False Positive Rate',fontsize=22)
plt.ylabel('True Positive Rate',fontsize=22)
plt.axes().set_aspect('equal')
plt.tick_params(axis='both', which='major', labelsize=16
plt.text(.05, -.25, txt, fontsize=22)
plt.savefig('%s_roc.pdf'%outprefix,bbox_inches='tight')
