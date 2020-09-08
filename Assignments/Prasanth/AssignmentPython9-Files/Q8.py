import sys
file_names=sys.argv[1:]
try:
    with open(file_names[0],'r') as f1:
        with open(file_names[1],'r') as f2:
            print(f1.read()==f2.read())
except Exception as err:
    print(err)