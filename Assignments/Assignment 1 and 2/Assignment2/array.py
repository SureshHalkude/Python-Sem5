
# arrays
b=arr.array("d",[1.1,2.2,3.3,4.4,5.5,6.6,7.7])
for i in range(0,7):
     print(b[i],end=" ")
     
# index

import array as arr

b=arr.array("d",[1.1,2.2,3.3,4.4,5.5,6.6,7.7])
for i in range(0,7):
     print(b[i],end=" ")
     
# count

import array as arr

b=arr.array("d",[1.1,2.2,3.3,4.4,5.5,6.6,7.7])
for i in range(0,7):
     print(b[i],end=" ")
     
     
# insert,append,remove,pop,reverse

import array as arr

b=arr.array("i",[11,22,33,44,55,66,77])
for i in range(0,7):
     print(b[i],end=" ")
print()
b.insert(7,88)
for i in (b):
     print(i,end=" ")
print()
b.append(111)
for i in (b):
    print(i,end=" ")
print()
b.remove(44)
for i in (b):
    print(i,end="-")
print()
b.pop()
for i in (b):
    print(i,end=" ")
print()
b.reverse()
for i in (b):
    print(i,end=" ")
    
# type

import array as arr

a=arr.array("i",[11,22,33,44])
print(a)
print(type(a))


# range

import array as arr
b=arr.array("i",[11,22,33,44,55,66,77])
for i in range(0,7):
     print(b[i],end=" ")