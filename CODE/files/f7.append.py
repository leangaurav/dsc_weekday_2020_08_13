# context manager: auto closing a file
with open("temp3.txt",'a') as f:
    print("pos", f.tell()) # pointer is at the  end
    print(f)
    for i in range(1,11):
        print(i,file = f)
    print("Status", f.closed)    
            
print("End")
print("Status", f.closed)