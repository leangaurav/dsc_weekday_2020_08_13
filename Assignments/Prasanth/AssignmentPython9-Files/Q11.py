import sys
file_name=sys.argv[1:]
count=0
words=[]
try:
    with open(file_name[0],'r') as f:
        for line in f:
            for word in line.split():
                words.append(sorted(word))
    words.sort()
    for w in range(1,len(words)):
        if words[w] == words[w-1]:
            count+=1
    print(count)
except Exception as err:
    print(err)