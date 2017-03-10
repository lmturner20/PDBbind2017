from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import is_aa
from Bio.PDB.Polypeptide import three_to_one

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

p= PDBParser(PERMISSIVE=1,QUIET=1)

firstName = "1pyg"
secondName = "4ouj"
firstHandle= "/home/dkoes/PDBbind/general-set-with-refined/1pyg/1pyg_rec.pdb"
secondHandle= "/home/dkoes/PDBbind/general-set-with-refined/4ouj/4ouj_rec.pdb"
firstStructure=p.get_structure(firstName,firstHandle)
secondStructure=p.get_structure(secondName,secondHandle)
firstSeq=getResidueString(firstStructure)
secondSeq=getResidueString(secondStructure)

score = pairwise2.align.globalxx(firstSeq, secondSeq, score_only=True)
length= max(len(firstSeq), len(secondSeq))
distance = (length-score)/length
print(firstName, secondName, distance)

#1pyg /home/dkoes/PDBbind/general-set-with-refined/1pyg/1pyg_rec.pdb
#4ouj /home/dkoes/PDBbind/general-set-with-refined/4ouj/4ouj_rec.pdb
