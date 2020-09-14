import sys
from os import path

def help():
	print("Invalid arguments")
	print("Usage: python FileCopy.py <file_1> <file_2>")
	exit(1)

def copy(file1, file2):
	try:
		with open(file1, 'r') as reader:
			with open(file2,'w') as writer:
				for i in reader:
					writer.write(i)

	except err:
		print("Error in reading and writing: ",str(err))
		exit(1)


def checkExistence(file1, file2):
	if path.isfile(file1) and not path.exists(file2):
		help()	

if len(sys.argv)!=3:
	help()
else:
	checkExistence(sys.argv[1], sys.argv[2])
	copy(sys.argv[1], sys.argv[2])



