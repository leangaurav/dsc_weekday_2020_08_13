'''
Task7: Modify the above program to count the occurrence of each symbol i.e. count of alphabet ‘a’,
count of spaces, count of commas and so forth.
'''
Task = "\nTask7: Count the occurrence of each symbol:"
print(Task + "\n" + "-"*len(Task))

import sys

if len(sys.argv) < 2:
    print("Usage: Python CountFileSymbols.py <Filename>")
else:
    try:
        fFrom = open(sys.argv[1], "r")
    except Exception as error:
        print(f"Error opening file: {sys.argv[1]}\n", error)
        exit()
    
    Symbol_Count_Dict = {}
    for c in fFrom.read():
        if c in Symbol_Count_Dict:
            Symbol_Count_Dict[c] = Symbol_Count_Dict[c]+1
        else:
            Symbol_Count_Dict[c] = 1

    print(Symbol_Count_Dict)
    
    fFrom.close()
