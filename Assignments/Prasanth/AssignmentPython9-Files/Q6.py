import sys
file_name=sys.argv[1:]
try:
    with open(file_name[0],'r') as f:
        print(f.read().count(" "))
except Exception as err:
    print(err)