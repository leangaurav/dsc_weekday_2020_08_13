'''
Task11: Update the program again to count and print number of anagrams in the file.
'''
Task = "\nTask11: Update the program again to count and print number of anagrams in the file:"
print(Task + "\n" + "-"*len(Task))

import sys

if len(sys.argv) < 2:
    print("Usage: Python CountAnagrams.py <Filename>")
else:
    try:
        fFrom = open(sys.argv[1], "r")
    except Exception as error:
        print(f"Error opening file: {sys.argv[1]}\n", error)
        exit()
    
    Anagrams_Count_Dict = {}
    Anagrams_Count = 0
    lWords = fFrom.read().split()
    for Word in lWords:
        for NextWord in lWords:
            if sorted(Word) != sorted(NextWord) or Word == NextWord: #Not Anagram
                continue
            else: #Anagram
                if Word in Anagrams_Count_Dict:
                    if NextWord not in Anagrams_Count_Dict[Word]:
                        Anagrams_Count_Dict[Word].append(NextWord)
                else:
                    Anagrams_Count_Dict[Word] = []
                    Anagrams_Count_Dict[Word].append(NextWord)
                    Anagrams_Count += 1
    
    print("Number of Anagrams = ", Anagrams_Count)
    print(Anagrams_Count_Dict)
    
    fFrom.close()
