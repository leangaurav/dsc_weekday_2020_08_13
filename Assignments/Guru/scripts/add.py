import sys

l=len(sys.argv)

n=sys.argv[1:]
print(n)

s = 0
for i in range(1,l):
    print(i)
   # if int(n[i]).isdigit():
   #   s += int(n[i])
   #else:
   #    print("Enter only numbers")
print(s)

   
    
