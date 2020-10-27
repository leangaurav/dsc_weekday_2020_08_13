import sys
import string

try:
    if len(sys.argv) == 2:
        source_file = sys.argv[1]
    else:
        source_file = input("Enter a file name : ")
        
    count=0
    words=[]

    with open(source_file,'r') as f:
        for line in f:
            for word in line.split():
                word = word.lower()
                words.append(sorted(word))   # sort letters with in the word and add to list words. 
#     print(words)
#     print()
    words.sort()                             # sort all the words in the list in place 
#     print()
#     print(words)
    for w in range(1,len(words)):
        if words[w] == words[w-1]:
#             print(words[w])
            count+=1
    print("The number of anagrams in file {} is {}".format(source_file,count))
except Exception as err:
    print(err)