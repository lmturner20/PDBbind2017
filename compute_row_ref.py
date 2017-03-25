
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import is_aa
from Bio.PDB.Polypeptide import three_to_one
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
import argparse
import sys
import glob

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
    return seq

if __name__ == '__main__':
    for handle in glob.glob('/home/dkoes/PDBbind/refined-set/*/*_rec.pdb'):
        segments = handle.split("/")
	name = segments[5]
        structure = p.get_structure(name, handle)
        seq=getResidueString(structure)

        for secondHandle in glob.glob('/home/dkoes/PDBbind/refined-set/*/*_rec.pdb'):
            data= secondHandle.split("/")
            secondName = data[5]
            secondStructure = p.get_structure(secondName, secondHandle)
            secondSeq=getResidueString(secondStructure)
            score =  pairwise2.align.localdx(v, w, matlist.blosum62, score_only=True)
            length= max(len(seq), len(secondSeq))
            distance = (length-score)/length
            fname = "/home/lmt72/PDBdistancesRef"+name+".distances"
            f = open('fname', 'w')
            f.write(secondName, distance)
