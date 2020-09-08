with open("Q1.txt", 'w') as f:
    f.write(",".join(list(map(lambda x: chr(x), range(65,91)))))