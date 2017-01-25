with open('Problem_Ligands') as infile:
	strings = infile.readLines()
infile.close()

strings = [ name[0:3] for name in strings]

for item in strings:
    smiItem = item + "_lig.smi"
    sdfItem = item + "_lig.sdf"
    babel --gen3D /home/dkoes/PDBbind/general-set-except-refined/item/smiItem /home/dkoes/PDBbind/general-set-except-refined/item/sdfItem
