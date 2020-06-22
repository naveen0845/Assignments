
#factorial using function



def factorial(num):
	if(num==1):
		return num
	else:
		return num*factorial(num-1)
num=int(input("enter the number"))
if(num<0):
	print("number entered is negative")
elif(num==0):
	print("factorial of zero is 1")
else:
	print("factorial of",num,"is",factorial(num))
	
	
	
	
#maximum of three using function


def maximum(a,b,c):
	if(a>b)and(a>c):
		print("a is max")
	elif(b>a)and(b>c):
		print("b is max")
	else:
		print("c is max")
maximum(5,6,7)



#given number in range or not

def search_elementa(a,x):
	if a in range(0,x+1):
		print("a is in range")
	else:
		print("a is not in range")
search_elementa(5,6)



	
