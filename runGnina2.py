import os
infile = open('dock180.txt', 'r')
string = infile.readline()
    
while string !="":
	string = string[0:4]
	pdbItem = "/home/dkoes/PDBbind/general-set-except-refined/"+string + "/" + string + "_rec.pdb"
  gninaItem = "/home/dkoes/PDBbind/general-set-except-refined/"+string + "/" + string + "_rec.gninatypes"
	cmd1 = ("gninatyper " + pdbItem + " " + gninaItem)
	os.system(cmd1)
	print(string)
	string = infile.readline()

infile.close()
