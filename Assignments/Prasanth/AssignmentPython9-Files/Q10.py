import sys
file_name=sys.argv[1:]
count=0
try:
    with open(file_name[0],'r') as f:
        for line in f:
            for word in line.split():
                if word.lower() == word.lower()[::-1]:
                    count+=1
    print(count)
except Exception as err:
    print(err)