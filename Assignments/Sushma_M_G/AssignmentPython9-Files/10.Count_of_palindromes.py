f = open("Palindrome.txt",'r')
content = f.read()
List_of_words = content.split()

Count = 0

for i in List_of_words:
    if i.casefold() == i[::-1].casefold():
        Count = Count + 1
        #List_of_Palindromes = i

print("The count of Palindromes in file",Count)
#print("The Palindromes in file",List_of_Palindromes)

f.close()