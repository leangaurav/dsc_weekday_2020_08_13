
try:
    n = int(input())
except ValueError:
    n = 0

try:
    a = [1,2,3]
    if n >= len(a):
        exit()
    else:
        print(a[n])
except:
    print("Somethhing went wrong")

print("End")