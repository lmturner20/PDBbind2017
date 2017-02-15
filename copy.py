import os
infile = open('FinalRefSet', 'r')
    
for string in infile:
	string = string[0:4]
	dir1 = "/home/dkoes/PDBbind/general-set-except-refined/" + string
	dir2 = "/home/dkoes/PDBbind/refined-set/" + string
	cmd1 = ("cp -R " + dir1 + " " + dir2)
	os.system(cmd1)

infile.close()
