from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import is_aa
from Bio.PDB.Polypeptide import three_to_one
from Bio import pairwise2

def getResidueString(structure):
    seq=''
    for model in structure:
	for residue in model.get_residues():
	    if is_aa(residue.get_resname(), standard=True):
		seq+=(three_to_one(residue.get_resname()))
	    else:
		resname = residue.get_resname()
		if resname == 'HIE' or resname == 'HID': seq+=('H')
		elif resname == 'CYX' or resname == 'CYM': seq+=('C')
		else: seq+=('X')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input',type=str,required=True)
    p= PDBParser(PERMISSIVE=1,QUIET=1)

    file = open(args.input)
    for line in file.readlines():
	data= line.split(" ")
	firstName = data[0]
        secondName = data[1]
        firstHandle= ("/home/dkoes/PDBbind/general-set-with-refined/%s/%s_rec.pdb" %(firstName))
        secondHandle= ("/home/dkoes/PDBbind/general-set-with-refined/%s/%s_rec.pdb" %(secondName))
        firstStructure=p.get_structure(firstName,firstHandle)
        secondStructure=p.get_structure(secondName,secondHandle)
        firstSeq=getResidueString(firstStructure)
        secondSeq=getResidueString(secondStructure)

        score = pairwise2.align.globalxx(firstSeq, secondSeq, score_only=True)
        length= max(len(firstSeq), len(secondSeq))
        distance = (length-score)/length
        print firstName, secondName, distance
