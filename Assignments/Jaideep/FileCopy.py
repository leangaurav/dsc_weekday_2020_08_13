'''
Task4: Write a program to read a file and copy it into a new file.
'''
Task = "\nTask4: Write a program to read a file and copy it into a new file:"
print(Task + "\n" + "-"*len(Task))

import sys

if len(sys.argv) < 3:
    print("Usage: Python FileCopy.py <From Filename> <To Filename>")
else:
    try:
        fFrom = open(sys.argv[1], "r")
    except Exception as error:
        print(f"Error opening file: {sys.argv[1]}\n", error)
        exit()
    
    fTo = open(sys.argv[2], "w")
    fTo.write(fFrom.read())
    
    fFrom.close()
    fTo.close()
