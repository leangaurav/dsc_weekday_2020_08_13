import sys
file_name=sys.argv[1:]
try:
    with open(file_name[0],'r') as f1:
        copiedFileName="_copy.".join(file_name[0].split("."))
        with open(copiedFileName,'w') as f2:
            f2.write(f1.read().swapcase())
except Exception as err:
    print(err)