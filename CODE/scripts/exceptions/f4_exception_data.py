print("start")

try:
    n = int(input("Enter a num: "))
    print("n=", n)
    r = 4//n
    print("r=", r)
except ValueError as err: # exception handlers
    print("Invalid value: ", err)
except ZeroDivisionError as err: # exception handlers
    print("Don't give zeroes: ", err)
