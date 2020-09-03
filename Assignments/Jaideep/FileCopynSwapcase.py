'''
Task5: Write a program to read a file and copy the contents to a new file such that the case gets reversed.
i.e. upper case becomes lower case and vice versa.
'''
Task = "\nTask5: Write a program to read a file and copy the contents to a new file and reverse case:"
print(Task + "\n" + "-"*len(Task))

import sys

if len(sys.argv) < 3:
    print("Usage: Python FileCopynSwapcase.py <From Filename> <To Filename>")
else:
    try:
        fFrom = open(sys.argv[1], "r")
    except Exception as error:
        print(f"Error opening file: {sys.argv[1]}\n", error)
        exit()
    
    fTo = open(sys.argv[2], "w")
    # fTo.write(fFrom.read().swapcase()) #Method1
    #Method2
    for c in fFrom.read():
        if c.isupper():
            c.lower()
        else:
            c = c.upper()
        fTo.write(c)
    
    fFrom.close()
    fTo.close()
