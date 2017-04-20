import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sklearn, argparse
import sklearn.metrics

parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('-g','--globe',type=str,required=True,help="Global pid")
parser.add_argument('-l','--chain',type=str,required=True,help="Local pid")
parser.add_argument('-r','--random',type=str,required=True,help="Random pid")
args = parser.parse_args()

globepid = args.globe
globef = open('/net/pulsar/koes/lmt72/PDBbind/global.finaltest,'a')
globe0 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+globepid+'.0.finaltest','r')
for line in globe0:
    globef.write(line)
globe0.close()
globe1 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+globepid+'.1.finaltest','r')
for line in globe1:
    globef.write(line)
globe1.close()
globe2 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+globepid+'.2.finaltest','r')
for line in globe2:
    globef.write(line)
globe2.close()
globef.close()

chainpid = args.chain
chainf = open('/net/pulsar/koes/lmt72/PDBbind/local.finaltest,'a')
chain0 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+chainpid+'.0.finaltest','r')
for line in chain0:
    chainf.write(line)
chain0.close()
chain1 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+chainpid+'.1.finaltest','r')
for line in chain1:
    chainf.write(line)
chain1.close()
chain2 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+chainpid+'.2.finaltest','r')
for line in chain2:
    chainf.write(line)
chain2.close()
chainf.close()

randompid = args.random
randomf = open('/net/pulsar/koes/lmt72/PDBbind/random.finaltest,'a')
random0 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+randompid+'.0.finaltest','r')
for line in random0:
    randomf.write(line)
random0.close()
random1 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+randompid+'.1.finaltest','r')
for line in random1:
    randomf.write(line)
random1.close()
random2 = open('/net/pulsar/koes/dkoes/tmp/PDBbind/refmodel3.'+randompid+'.2.finaltest','r')
for line in random2:
    randomf.write(line)
random2.close()
randomf.close()

gtrue = []
gscore = []
globef = open('/net/pulsar/koes/lmt72/PDBbind/global.finaltest,'r')
for line in globef:
    data= line.split()
    gtrue += data[0]
    gscore += float(data[1].strip())
fpr, tpr, _ = sklearn.metrics.roc_curve(gtrue,gscore)
auc = sklearn.metrics.roc_auc_score(gtrue,gscore)

ltrue = []
lscore = []
chainf = open('/net/pulsar/koes/lmt72/PDBbind/local.finaltest,'r')
for line in chainf:
    data= line.split()
    ltrue += data[0]
    lscore += float(data[1].strip())
fpr2, tpr2, _ = sklearn.metrics.roc_curve(ltrue,lscore)
auc2 = sklearn.metrics.roc_auc_score(ltrue,lscore)

rtrue = []
rscore = []
randomf = open('/net/pulsar/koes/lmt72/PDBbind/random.finaltest,'r')
for line in randomf:
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
plt.tick_params(axis='both', which='major', labelsize=16
plt.text(.05, -.25, txt, fontsize=22)
plt.savefig('%s_roc.pdf'%outprefix,bbox_inches='tight')
