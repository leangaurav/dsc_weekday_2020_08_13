print("\n\n READ")
with open("lines.txt", "r+") as file:
    r = file.read()
    print(r, type(r))
    file.seek(0)
    file.write("ABCD")

# r, rb, r+, rb+ 0
# w, wb, w+, wb+ 0
# a...           End
print()    
with open("lines.txt", "rb") as file:
    r = file.read()
    print(r, type(r))
