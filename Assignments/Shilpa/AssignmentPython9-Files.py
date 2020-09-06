#To run the whole assignment please pass value as mentioned below to get the o/p in one go.
#python file1.py "textfile1" "textfile2"

#Q1 Print the alphabets in the file
from string import ascii_lowercase

print("O/P will be written in the file")
with open("File1.txt","w") as wfile:
    for letter in ascii_lowercase:
        print(letter,file=wfile,end=" ")
print("End of Q1 \n")


# Q2 WAP to read the file and print on the commandline
with open("File1.txt","r") as rfile:
    lstfile=list(rfile)
    print(lstfile)
print("End of Q2 \n")

#Q3 WAP to predict the output
f=open("file1.txt","w")
f.write("write something in the file \n Write as much as you want")
f.close()

f=open("file1.txt","r")
print(f.tell())
print(f.read(4))
print(f.tell())
print("End of Q3 \n")

#Q4 WAP to read file and write a content into a new file

print("O/P will be written in the file")
with open("File1.txt","r") as rfile:
    filecontent=rfile.readlines()

with open("File2.txt","w") as wfile:
    for line in filecontent:
        print(line,file=wfile,end=" ")
print("End of Q4 \n")

#Q5 WAP to read file and write a content into a new file, and change the letter case Upper->Lower and Lower->Upper

print("O/P will be written in the file")
with open("File1.txt","r") as rfile:
    filecontent=rfile.readlines()

with open("File2.txt","w") as wfile:
    for line in filecontent:
            print(line.swapcase(),file=wfile,end=" ")

print("End of Q5 \n")
# Q6 WAP to take the file name at command line argument and count the space.

import sys

filename=str(sys.argv[1])

print("filename" , filename)
if len(filename) > 1 :
    with open(filename,"r") as rfile:
        filecontent=rfile.readlines()
spcnt=0
for lst in filecontent:
    spcnt = spcnt + lst.count(" ")

print(f"No of space in file {filename} is {spcnt}")
print("End of Q6 \n")

#Q7 WAP to take the file name at command line argument and count the space,alphabets,comma and digit.

import sys


filename=str(sys.argv[1])

print("filename" , filename)
if len(filename) > 1 :
    with open(filename,"r") as rfile:
        filecontent=rfile.readlines()

spcnt = 0
alphacnt = 0
numcnt = 0
spchcnt=0

for lst in filecontent:
    spcnt = spcnt + lst.count(" ")
    alphacnt=alphacnt+sum(1 for c in lst if c.isalpha())
    numcnt=numcnt+sum(1 for c in lst if c.isdigit())
    spchcnt=spchcnt=sum(1 for c in lst if c in "[@_!#$%^&*()<>?/|}{~:]-")

print(f"No of space in file {filename} is {spcnt}")
print(f"No of alphabets in file {filename} is {alphacnt}")
print(f"No of number in file {filename} is {numcnt}")
print(f"No of special char in file {filename} is {spchcnt}")
print("End of Q7 \n")

#Q8 WAP to check the content of two files and print true or false if the content is same

import sys

lst=[]  
for file in sys.argv:
    if file != "File1.py":
        with open(file,"r") as file1:
            strfile=file1.readlines()
            lst.append(strfile)

if len(lst) > 1 and lst[0] == lst[1]:
    print("File content is same")
else:
    print("File content is not same")
    
print("End of Q8 \n")   
    
#Q9 WAP to count the no of words in the file

import sys


filename=str(sys.argv[1])

print("filename" , filename)
strfile=""
if len(filename) > 1 :
    with open(filename,"r") as rfile:
        for line in rfile:
            strfile=strfile.join(str(line))
        print(strfile)

print(f"No of word in file {filename} is {len(strfile.split(' '))}")
print("End of Q9 \n") 

#Q10 WAP to count the no of pallindrome in the file

import sys

filename=str(sys.argv[1])

pcount=0
strword=""
print("filename1" , filename)

with open(filename,"r") as rfile:
    for line in rfile:
        pcount+=sum(1 for word in line.split(' ') if word == word[::-1])
        strword = strword.join("," + str(word) for word in line.split(' ') if word == word[::-1] )
    print(strword[1::])
        
print(f"No of palindromes word in file {filename} is {pcount}")
print("End of Q10 \n") 
    
#Q11 WAP to count the no of anagrams in the file

import sys
from collections import Counter 

filename=str(sys.argv[1])

anagramcnt=0
strword=""
print("filename1" , filename)

with open(filename,"r") as rfile:
    for line in rfile:
        for word in line.split(" "):
            strword=strword + " " + "".join(str(c) for c in sorted(word.lower()))
    dictline = Counter(strword.split(" "))
#print(dictline)

anagramcnt = anagramcnt + sum(value for value in dictline.values()  if value > 1)
print(f"No of palindromes word in file {filename} is {anagramcnt}")
print("End of Q11 \n") 