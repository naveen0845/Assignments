#Finding largest and smallest numbers in list

l=sorted(input('enter the list'),reverse=False)
print(l)
print(l[0],'is an smallest number and the largest number is ',l[-1])



#Check a list is empty or not

l=input('enter the list elements')
if len(l)==0:
  print('the list is empty')
else:
  print('the list contains some elements ')



#To clone or copy the list

a=list(input('enter the list elements'))
b=a    
print(b)
a.append('h')
print(b)
print(a)



#Removing even numbers from a list¶

l=list(input('enter the elements of the list'))
for i in l:
  if int(i)%2==0:
    l.remove(i)
  else:
    pass
print(l)




#Copy the contents of a file to another file

import shutil
path= 'C:\\Users\\naveen\\Documents\\example1.txt'
target = 'C:\\Users\\naveen\\Documents\\example2.txt'
shutil(path,target)
f=open('example2.txt')
a=f.read()
print(a)



#sum of all the items in a list¶

l=list(input('enter the list elements'))
sum=0
for i in l:
  sum+=int(i)
print(sum)