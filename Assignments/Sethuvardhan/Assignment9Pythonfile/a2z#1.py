import string
alpha = list(string.ascii_lowercase)
with open('atoz.txt','w') as fl:
	for i in alpha:
		fl.write(i)