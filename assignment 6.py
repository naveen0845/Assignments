#binary to decimal 

n=str(input("enter the binary code"))
x=int(n,2)
print(x)



#fibonacci series 

a=0
b=1
n=int(input("enter no of elements"))
fibo=[ ]
for i in range(n):
	fibo.append(a)
	a,b=b,a+b
print(fibo)




#multiplication table

k=int(input("enter the number "))
for i in range(1,11):
	a=k*i
	print(a)
		
		
		
#GCD of two numbers

a=int(input("enter the first number"))
b=int(input("enter the second number"))
for i in range(a,b):
		if(a==0):
			print(f'{a} and {b}={gcd}')
while(b!=0):
	if(a>b):
		a=a-b
	else:
		b=b-a
gcd=a
print(f'{a} and {b}={gcd}')


		
		
		

