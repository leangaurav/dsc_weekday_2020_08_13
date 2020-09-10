#1. WAP to print in python that stores alphabets from a to z in text file
f = open("Print_a_to_z_file.txt",'w')
for i in range(97,123):
    print(chr(i),file = f,end = ' ' )

#f1 = open("Print_a_to_z_file.txt",'a')
#for j in range(65,91):
#    print(chr(j),file = f1,end = ' ')
    

