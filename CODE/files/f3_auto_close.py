# context manager: auto closing a file
with open("temp1.txt",'w') as f:
    print("pos", f.tell())
    print(f)
    for i in range(1,11):
        print(i,file = f)
    print("Status", f.closed)    
            
print("End")
print("Status", f.closed)