'''
Task10: Update the above program to count the number of palindromes present in the file.
'''
Task = "\nTask10: Update the above program to count the number of palindromes present in the file:"
print(Task + "\n" + "-"*len(Task))

import sys

if len(sys.argv) < 2:
    print("Usage: Python CountPalindromes.py <Filename>")
else:
    try:
        fFrom = open(sys.argv[1], "r")
    except Exception as error:
        print(f"Error opening file: {sys.argv[1]}\n", error)
        exit()
    
    Palindrome_Count_Dict = {}
    Plalindrome_Count = 0
    lWords = fFrom.read().split()
    for Word in lWords:
        if Word != Word[::-1]: #Not Palindrome
            continue
        else: #Palindrome
            Plalindrome_Count += 1
            if Word in Palindrome_Count_Dict:
                Palindrome_Count_Dict[Word] += 1
            else:
                Palindrome_Count_Dict[Word] = 1
    
    print("Number of Palindromes = ", Plalindrome_Count)
    print(Palindrome_Count_Dict)
    
    fFrom.close()
