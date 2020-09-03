'''
Task6: Write a program that take a file name as command line argument, opens it and then counts
number of space characters in that file.
'''
Task = "\nTask6: Write a program that take a file name and count number of space characters in that file:"
print(Task + "\n" + "-"*len(Task))

import sys

if len(sys.argv) < 2:
    print("Usage: Python CountFileSpaces.py <Filename>")
else:
    try:
        fFrom = open(sys.argv[1], "r")
    except Exception as error:
        print(f"Error opening file: {sys.argv[1]}\n", error)
        exit()
    
    #nSpaces = fFrom.read().count(" ")  #Method1
    
    #Method2
    nSpaces = 0
    for c in fFrom.read():
        if c == " ":
            nSpaces+=1
    
    print("No. of Spaces = ", nSpaces)
    
    fFrom.close()
