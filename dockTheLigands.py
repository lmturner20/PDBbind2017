import os
infile = open('Problem_Ligands', 'r')
string = infile.readline()
    
while string !=' ':
	string = string[0:4]
	pdbItem = "/home/dkoes/PDBbind/general-set-except-refined/"+string + "/" + string + "_rec.pdb"
	sdfItem = "/home/dkoes/PDBbind/general-set-except-refined/"+string + "/" + string + "_lig.sdf"
	pocketItem = "/home/dkoes/PDBbind/general-set-except-refined/"+string + "/" + string + "_pocket.pdb"
	dockedItem = "/home/dkoes/PDBbind/general-set-except-refined/"+string + "/" + string + "_docked.sdf.gz"
	cmd1 = ("smina -r " + pdbItem + " -l " + sdfItem + " --autobox_ligand " + pocketItem + " --num_modes 25 --seed 0 -o " + dockedItem + " --cpu 8 --exhaustiveness 50")
	os.system(cmd1)
	string = infile.readline()

infile.close()
