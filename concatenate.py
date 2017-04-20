import argparse

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
