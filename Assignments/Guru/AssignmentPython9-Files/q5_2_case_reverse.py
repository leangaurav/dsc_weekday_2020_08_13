
source_file = input("Enter a source file name: ")

dot_index = source_file.rfind(".")
target_file = source_file[:dot_index] + "_reversing_case" + source_file[dot_index:]

with open(source_file,"r") as rfile:
    filecontent=rfile.readlines()

with open(target_file,"w") as wfile:
    for line in filecontent:
            print(line.swapcase(),file=wfile,end=" ")