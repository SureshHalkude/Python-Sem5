#type() method
p=(1,2,3,4,5,)
print(type(p))
print(p)


#Count() method
t2=(1,2,3,4,5,3,7,1,11,4444,6,7,8,99,3,10,2.5,12,3)
print(t2.count(3))

#index() method
t3=(1,2,3,4,5,3,7,1,11,4444,6,7,8,99,10,2.5,12)
print(t3.index(3))

# len,sorted,max,min,sum
t1=(9,8,7,6,5,4,3,2,1,10,11,12,13,14,15)
print(t1)
print(len(t1))
print(sorted(t1))
print(max(t1))
print(min(t1))
print(sum(t1))

# iterating
t5 = (11, 22, 33, 44, 55, 66, "right", 4.7, 8.8)
for i in t5:
    print(i, end=" ")  # Note the use of # for comments

# printing tuple
t6=(11,22,33,44,55,66,"right",4.6,7.8)
print(t6)