'''
Task9: WAP to count the number of words in a file.
'''
Task = "\nTask9: WAP to count the number of words in a file:"
print(Task + "\n" + "-"*len(Task))

import sys

if len(sys.argv) < 2:
    print("Usage: Python CountWords.py <Filename>")
else:
    try:
        fFrom = open(sys.argv[1], "r")
    except Exception as error:
        print(f"Error opening file: {sys.argv[1]}\n", error)
        exit()
    
    Word_Count_Dict = {}
    lWords = fFrom.read().split()
    for Word in lWords:
        if Word in Word_Count_Dict:
            Word_Count_Dict[Word] += 1
        else:
            Word_Count_Dict[Word] = 1
    
    print(Word_Count_Dict)
    
    fFrom.close()
