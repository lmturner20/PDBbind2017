import os
with open('Problem_Ligands') as infile:
	strings = infile.readLines()
infile.close()

strings = [ name[0:3] for name in strings]

for item in strings:
    smiItem = "/home/dkoes/PDBbind/general-set-except-refined/"+item + "/" + item + "_lig.smi"
    sdfItem = "/home/dkoes/PDBbind/general-set-except-refined/"+item + "/" + item + "_lig.sdf"
    cmd1 = "babel --gen3D smiItem sdfItem"
    os.system(cmd1)
