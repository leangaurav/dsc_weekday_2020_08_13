print("start")
try:
    n = int(input("Enter a num: "))
    print("n=", n)
    r = 4//n
    print("r=", r)
except ValueError: # exception handlers
    print("Invalid value")
except ZeroDivisionError: # exception handlers
    print("Don't give zeroes")
