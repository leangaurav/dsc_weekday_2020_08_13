# context manager: auto closing a file
with open("temp2.txt",'w') as f:
    f.write("some text")
    f.write("some text2") # always writes strings
    print(10, file=f)
    print(10, file=f)
            
print("End")