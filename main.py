import sys
filename = sys.argv[1]

if(not filename):
	raise sys.exit("No file")

f = open(filename, "r")

startLine = "SET SQL_MODE = \"NO_AUTO_VALUE_ON_ZERO\";\nSET time_zone = \"+00:00\";\n"

startNewFile = False
currentFile = None

def createFile(line):
	fileName = line[14:]
	fileName = fileName[:-2]
	fileName = fileName + ".sql"
	print fileName
	if currentFile:
		currentFile.close()
	newFile = open(fileName, "w")
	newFile.write(startLine)
	return newFile

for line in iter(f):
    if "-- Database:" in line:
    	currentFile = createFile(line)
    if currentFile:
    	currentFile.write(line)

f.close()