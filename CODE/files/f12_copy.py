import sys

# argparse
if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    print("invalid syntax")  

try:
    # generat file name
    dot_index = file_name.rfind(".") # "f1_file.py"
    file_name_copy = file_name[:dot_index] + "_copy" + file_name[dot_index:]
    print("copying {} to {}".format(file_name, file_name_copy))
    
    # copy contents
    with open(file_name, 'r') as file1:
        print(file1)
        print(dir(file1))
        with open(file_name_copy, 'w') as file2:
            file2.write(file1.read())
except FileNotFoundError:
    print("File not found!!")
