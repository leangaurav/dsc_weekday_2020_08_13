try:
    n = int(input("Enter a num: "))
    print("n=", n)
    r = 4//n
    print("r=", r)
except: # generic  exception -> don't use in practice
    print("Please enter a number only!")
