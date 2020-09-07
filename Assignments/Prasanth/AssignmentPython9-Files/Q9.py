import sys
file_name=sys.argv[1:]
try:
    with open(file_name[0],'r') as f:
        for line in f:
            for word in line.split():
                print(word)
except Exception as err:
    print(err)