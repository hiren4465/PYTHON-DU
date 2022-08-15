num1 = int(input("Enter 1st number : "))
num2= int(input("Enter 2nd number : "))
char= input("Enter character : ")

if char=='+' : # 
	c = num1 + num2
if char=='-':
	c = num1 - num2
if char=='*':
	c = num1 * num2
if char=='/':
	c = num1 / num2

print('{0}+{1}={2} '.format(num1,num2,c))
