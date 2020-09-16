# WAP to print 1-10 to a file.. numbers.txt
f = open("temp1.txt",'w')
print(f)
for i in range(1,11):
        print(i,file = f)

input()
f.close()