import os
infile = open('FinalGenSet.txt', 'r')
string = infile.readline()
    
while string !=' ':
	string = string[0:4]
	dir1 = "/home/dkoes/PDBbind/general-set-except-refined/" + string
	dir2 = "/home/dkoes/PDBbind/general-set-with-refined/" + string
	cmd1 = ("cp -r " + dir1 + dir2)
	os.system(cmd1)
	string = infile.readline()

infile.close()
