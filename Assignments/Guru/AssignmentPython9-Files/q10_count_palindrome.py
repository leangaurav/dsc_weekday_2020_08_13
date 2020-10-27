import sys
import string

try:
    if len(sys.argv) == 2:
        source_file = sys.argv[1]
    else:
        source_file = input("Enter a file name : ")

    pcount = 0
    words = []
    with open(source_file,'r') as s_file:
        for line in s_file:
            for word in line.split():
                word = word.lower()
                if word == word[::-1]:
                    pcount += 1
                    words.append(word)
    print(words)
    print("Numer of palindrome words in file {} is {}".format(source_file,pcount))

except Exception as err:
    print(err)