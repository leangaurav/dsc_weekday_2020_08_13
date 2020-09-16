'''
Task8: Write a script called diff.py that take two file names as arguments and checks if the content of
both the files is same and prints true or false.
'''
Task = "\nTask8: Write a script called diff.py to compare two files:"
print(Task + "\n" + "-"*len(Task))

import sys

if len(sys.argv) < 3:
    print("Usage: Python diff.py <Filename1> <Filename2>")
else:
    try:
        fFile1 = open(sys.argv[1], "r")
        fFile2 = open(sys.argv[2], "r")
    except Exception as error:
        print(f"Error opening file: {sys.argv[1]} or {sys.argv[2]}\n", error)
        exit()
    
    bDifferent = False
    if fFile1.read() == fFile2.read():
        bDifferent = True
    print(bDifferent)
    
    fFile1.close()
    fFile2.close()
