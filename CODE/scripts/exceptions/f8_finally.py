
try:
    n = int(input())
except ValueError:
    print("ValueError")
    n = 0

try:
    a = [1,2,3]
    print(a[n])
except:
    print("Somethhing went wrong")
else:
    print("No exceptions")
finally:
    print("Finally, n is", n)

print("End")