# specific handlers should  come first
print("start")

try:
    n = int(input("Enter a num: "))
    print("n=", n)
    r = 4//n
    a = [1,2,3]
    print("r=", r)
    print("value", a[n])
except ValueError as err: # exception handlers
    print("Invalid value: ", err)
except ZeroDivisionError as err: # exception handlers
    print("Don't give zeroes: ", err)
except Exception as err: # genric one should be at last
    print("Some unhanadled exception:", err)
