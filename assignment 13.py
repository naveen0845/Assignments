#Checking whether a string is stars with specified character

a=input('enter the string')
if a.lower().startswith('a'):
  print('the string stars with : a ')




#Index of the charactor in the string

i=a.index('a')
i1=a.index('a',1)
print(i)
print(i1)




#Iterate over the dictionary using for loop

n={'a':1,'b':2,'c':4,'d':5}
for i,j in n.items():
  print(i,':',j,end=',')




#Removing keys from a dictionary

d={'a':4,'b':1,'c':3,'d':5,'e':0}
print(d)
del d['e']  
print(d)