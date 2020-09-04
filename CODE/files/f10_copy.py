import sys
self_name = sys.argv[0]

with open(self_name, 'r') as file:
    content = file.read()
    print(content)