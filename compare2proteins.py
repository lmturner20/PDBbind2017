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
