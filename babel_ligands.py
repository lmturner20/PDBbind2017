with open('Problem_Ligands') as infile:
	strings = infile.readLines()
infile.close()

strings = [ name[0:3] for name in strings]

for item in strings:
    smiItem = item + ".smi"
    sdfITem = item + ".sdf"
    babel -gen3D smiItem sdfItem
