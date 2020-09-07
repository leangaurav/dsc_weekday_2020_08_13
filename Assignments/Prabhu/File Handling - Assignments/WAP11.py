#  Update the above program to count the number of anagrams present in the file.  

src_file=open("random.txt","r")
content=src_file.read()

src_words = content.split()
tgt_words = src_words

n=len(src_words)

cnt=0

for i in range(0,n) :
    for j in range(i+1,n) :
        if len(src_words[i])==len(tgt_words[j]):
            if src_words[i]!=tgt_words[j]:
                if sorted(src_words[i])==sorted(tgt_words[j]):
                    cnt+=1

print("No. of. Anagrams in the file are ", cnt)

src_file.close()