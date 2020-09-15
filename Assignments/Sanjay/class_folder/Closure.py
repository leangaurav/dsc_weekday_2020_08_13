
def func():
	dollar_value=71
	counter=0
	
	def conversion_INR(x):
		counter+=1
		return dollar_value*x,counter
	return conversion_INR

convert=func()
print("INR for $10 is: ", convert(10))