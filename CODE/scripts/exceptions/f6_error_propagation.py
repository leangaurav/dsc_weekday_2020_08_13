# specific handlers should  come first

def func():
    try:
        n = int(input("Enter a num: "))
        print("n=", n)
        r = 4//n
        a = [1,2,3]
        print("r=", r)
        print("value", a[n])
    except ValueError as err: # exception handlers
        print("Invalid value: ", err)
    print("Success func")

def func1():
    try:
        func()
    except ZeroDivisionError as err: # exception handlers
        print("Don't give zeroes: ", err)
    print("Success func1")

# starts here
try:
    func1()
except Exception as err: # genric one should be at last
    print("Some unhanadled exception:", err)

func() # this crashes and prints a stack trace