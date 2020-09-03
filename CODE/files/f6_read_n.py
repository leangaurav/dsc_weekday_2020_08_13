# resd
with open("temp2.txt",'r') as f:
    
    while True:
        s = f.read(5)
        if len(s) == 0:
            break
        print(s, f.tell())

    print()
    print("re-read: ", f.read())
    
    print()
    f.seek(0)
    print("re-read: ", f.read())
 
print("End")