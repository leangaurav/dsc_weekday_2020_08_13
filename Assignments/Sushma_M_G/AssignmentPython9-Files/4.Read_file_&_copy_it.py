f = open("Print_a_to_z_file.txt","r")
content = f.read()

f1 = open("copy_of_Print_a_to_z_file.txt","w")
f1.write(content)

f.close()
f1.close()