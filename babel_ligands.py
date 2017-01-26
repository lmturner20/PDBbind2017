import os
infile = open('Problem_Ligands', 'r')
string = infile.readLine()
    
while line !=' ':
	string = string[0:3]
	smiItem = "/home/dkoes/PDBbind/general-set-except-refined/"+item + "/" + item + "_lig.smi"
	sdfItem = "/home/dkoes/PDBbind/general-set-except-refined/"+item + "/" + item + "_lig.sdf"
	cmd1 = "babel --gen3D smiItem sdfItem"
	os.system(cmd1)
	string = infile.readLine()

infile.close()
