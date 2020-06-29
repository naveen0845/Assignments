#Read an entire text file

f=open('example.txt')
f.seek(0)
x=f.read()
print(x)



#Append text to a file and display the text

f=open('example2.txt','a+')
f.write('\nhello world')
f.write('\nmy name is naveen')
f.seek(0)
print(f.read())



#Read a file line by line

f=open('example3.txt')
x=f.readlines()
f.seek(0)
print(x)



#Read contents of a file using for loop

f=open('example3.txt','r+')
lines=f.readlines()
for l in lines:
    print(l)
    
    
  
      
#5.Remove leading and traling spacesfrom a string

a=input('enter the string')
print(f'before appling strip function is : {a}')
print(f'after removing all lstrips and rstrips in string is : {a.strip()}')