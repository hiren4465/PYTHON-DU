num1 = int(input("Enter 1st number : "))
flag =0

for i in range(2,num1) :
	if num1%i==0 :
		flag=1
		break
if flag==1 :
	print('{} not prime'.format(num1))
else :
	print('{} is prime'.format(num1))