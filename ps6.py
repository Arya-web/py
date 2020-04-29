x = -1
y = 1

z = int(input("Enter no of values to print : "))
i = 0

while i < z :
	x = x+y
	print(x,end=' ')
	i = i + 1
	if i<z:
		y = x+y
		print(y,end=' ')
		i = i + 1

a = int(input("\nEnter no to be checked : "))

b = -1
c = 1
k = 0

while k < a:
	b = b + c 
	k = b
	if k<a :
		c = b + c
		k = c
	else :
		break
		
if k == a :
	print("Fibonacci no")
else :
	print("Not Fibonacci no")




