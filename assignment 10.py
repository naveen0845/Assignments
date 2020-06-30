#Open the file with try and except

try:
    f=open('example2.txt')
    print(f.read())
except:
    print('no file exist')
    
    
    
#Split the data in the file

f=open('example3.txt')
a=f.read()
print(a)
print(a.split())



#To read the contents in file using the with statement

with open('example2.txt') as f:
    a=f.read()
    print(a)
    
    
    
#To remove the file and Director

import os
os.getcwd()
import os   
file = 'example3.txt' 
location = 'C:\\Users\\Siva Krishna\\Documents'
path = os.path.join(location, file)   
os.remove(path)



#TO access elements in the list

l=[1,3,4,2]
print(len(l))
print(l[1])
l[3]='k'
print(l)



