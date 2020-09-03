'''
Task2: Write a program to read itself and print on the screen (Use Command Line Arguments).
'''
Task = "\nTask2: Write a program to read itself and print on the screen (Use Command Line Arguments):"
print(Task + "\n" + "-"*len(Task))

import sys

f = open(sys.argv[0], "r")
print(f.read())
f.close()
