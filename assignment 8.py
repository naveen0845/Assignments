#length of the string 

n=str(input("enter string"))
print("length of the given string",len(n))



#count no of char in string 

count=0
n=["naveen","suresh","ravi","krish"]
for i in n:
	count=count+1
print("there are",count,"character")



#no of "o" in hello world 

string="hello world"
char=str(input("enter the string to print"))
count=0
for i in range(len(string)):
	if(string[i]==char):
		count=count+1
print("total no of times the",char,"occured",count)



#upper case and lower case

a=str(input("enter the string"))
upper=a.upper()
lower=a.lower()
print("upper case:",upper)
print("lower case:",lower)



#sub string in string

a=str(input("enter the string"))
n=a.split()
print("sub string in string is:",n)



#comparing two strings 

str1=str(input("enter string1"))
str2=str(input("enter string2"))
if str1==str2:
	print("string are equal")
else:
	print("strings are not equal")
	
	
	
#deletion of char

n=str(input("enter the string"))
print(n.replace("n"," "))



#printing every character in string

n=str(input("enter the string"))
for i in n:
	print(i,"char in string",n)
	
	
	
#length of string without length function

n="refirgerator"
a=0
for i in n:
	a+=1
print(a)



#sub strings are present in string or not 

a=input('enter the string')
n=a.split()
c=0
for i in n:
  if len(i)==1:
    c+=1
  else:
    pass
if c in [0,1,2]:
  print('the string contains substrings')
else:
  print('the string does not have substrings')
	
	