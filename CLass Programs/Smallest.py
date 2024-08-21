a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
c=int(input("Enter the number:-"))

if(a<=b and a<=c):
    print("A is smaller..")
elif(b<=a and b<=c):
    print("B is smaller")
elif(c<=a and c<=b):
    print("C is smaller")
else:
    print("invalid")