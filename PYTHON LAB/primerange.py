num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

flag=0
for i in range(num1,num2+1) :
	for j in range (2,i) :
		if i%j==0 :
			flag=1
			break
	if flag==0 :
		
		print(i)