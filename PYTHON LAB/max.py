num1 = int(input("Enter 1st number : "))
num2= int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))

if num1 > num2 :
	if num1 > num3 :
		#print(num1 , " is gretest.") # 1st method
		print('{} is gretest.'.format(num1)) # 2nd method
	else :
		#print(num3 , " is gretest.") # 1st method
		print('{} is gretest.'.format(num3)) # 2nd method
else :
	if num2 > num3 :
		#print(num2 , " is gretest.") # 1st method
		print('{} is gretest.'.format(num2)) #2nd method
	else :
		#print(num3 , " is gretest.") # 1st method
		print('{} is gretest.'.format(num3)) #2nd method