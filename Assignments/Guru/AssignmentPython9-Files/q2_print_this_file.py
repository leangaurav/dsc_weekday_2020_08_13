# Q2 WAP to read the file itself and print on the screen (use the commandline arguments)
import sys
file_name = sys.argv[0]   # it takes this file name itself as argument

with open(file_name, 'r') as file:
    print(file.read()) 
#     s = file.read()
#     print(s)


# with open("file_alpha.txt","r") as rfile:
#     lstfile=list(rfile)
#     print(lstfile)
# print("End of Q2 \n")
    
    