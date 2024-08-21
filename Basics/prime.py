n1=int(input("Enter number:-"))
count=1
for i in range(1,n1):
     if(n1%i==0):
          count+=1
if(count==2):
     print("Prime number")
else:
    print("Not prime number")