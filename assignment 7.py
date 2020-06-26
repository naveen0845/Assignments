#adding n natural numbers

sum=0
i=0
n=int(input("enter the number"))
while(i<=n):
	sum=sum+i
	i=i+1
print(sum)




#counting even and odd

numlist=[]
even_count=0
odd_count=0
n=int(input("enter no of elements"))
for i in range(0,n):
	v=int(input("enter the values"))
	numlist.append(v)
for j in range(n):
	if(numlist[j]%2==0):
		even_count=even_count+1
	else:
		odd_count=odd_count+1
print("no of even",even_count)
print("no of odd",odd_count)



#print 0 to 6 except 3 and 6

for i in range(0,6):
	if(i%3!=0):
		print(i)
		
		
		
#square of numbers 

for i in [1,2,3,4,5]:
	square=i*i
	print(square)
	


#sum and average of n numbers

i=0
sum=0
n=int(input("enter n "))
while(i<=n):
	sum=sum+i
	i=i+1
	ave=sum/n
print("sum of given number=",sum)
print("average=",ave)
	
	
	

#reversing a number

number=int(input("enter the number"))
reverse=0
while(number>0):
	x=number%10
	reverse=(reverse*10)+x
	number=number//10
print("reverse of entered number is ",reverse)



#print odd number in given range

for i in range(10):
	if(i%2!=0):
		print(i)



#print no of digits in number


n=int(input("enter the digits"))
count =0
while(n>0):
	n=n//10
	count=count+1
print(count)



#palindrome or not 

n=int(input("enter the number"))
reverse=0
temp=n
while(n>0):
	dig=n%10
	reverse=(reverse*10)+dig
	n=n//10
if(temp==reverse):
	print("palindrome")
else:
	print("not palindrome")
	
	
	
#identity matrix

n=int(input("enter n"))
for i in range(0,n):
	for j in range(0,n):
		if i==j:
			print("1",sep=" ",end=" ")
		else:
			print("0",sep=" ",end=" ")
	print()
print()



#perfect number or not 

n=int(input("enter the number "))
sum=0
for i in range(1,n):
	if(n%i==0):
		sum+=i
if(sum==n):
	print("entered number",n,"is perfect")
else:
	print("entered number",n,"is not perfect")
	


	