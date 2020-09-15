import sys
def add_args(sysargs):
    sumval = 0
    try: 
        for i in sysargs[1:]:
           sumval+=int(i)
        return sumval
    except :
        print("Enter numbers only")
        
    
val=add_args(sys.argv)
if(val):
	print(val)

