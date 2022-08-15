num1 = int(input("Enter 1st number : "))

print("the factors of {} is :".format(num1), end=" ")
for i in range (1,num1+1) :
	if num1%i==0:
		print(i,end="  ")