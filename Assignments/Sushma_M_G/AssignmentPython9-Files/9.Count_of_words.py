f = open("copy_of_file.txt",'r')
content = f.read()

List_of_words = content.split()
print(List_of_words)
print("The Number of words",len(List_of_words))
