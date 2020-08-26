def myfunc1():
    """
    empty function doc
    this is second line
    """
    pass
   
def myfunc2():
    pass
    
print("func1")
print(myfunc1.__doc__)

print()
print("func2")
print(myfunc2.__doc__)


print()
print("HELP")
print(help(myfunc2))


print()
print("HELP1")
print(help(myfunc1))
    