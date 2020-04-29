x = int(input("Enter lower limit : "))
y = int(input("Enter upper limit : "))

for i in range(x,y+1):
	if i > 1 :
		for j in range(2,i):
			if i%j == 0 :
				break
		else:
			print(i,end=' ')

z = int(input("\nEnter natural no to be checked : "))
if z == 1 :
	print("Neither prime nor composite.")
else :
	for i in range(2,z) :
		if z%i == 0 :
			print("Non-Prime")
			break
	else:
		print("Prime")