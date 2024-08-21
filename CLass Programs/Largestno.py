a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
c=int(input("Enter the number:-"))

if(a>=b and a>=c):
    print("A is greater..")
elif(b>=a and b>=c):
    print("B is greater")
elif(c>=a and c>=b):
    print("C is gretaer")
else:
    print("invalid")