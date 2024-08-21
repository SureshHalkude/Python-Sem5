m1=int(input("enter the marks of 1st subject:-"))
m2=int(input("enter the marks of 2nd subject:-"))
m3=int(input("enter the marks of 3rd subject:-"))
m4=int(input("enter the marks of 4th subject:-"))

total_percntage=(100*(m1 + m2 + m3 + m4))/400

if(total_percntage>=40 and m1>=34 and m2>=34 and m3>=34 and m4>=34):
    print("You are passeed!!.",total_percntage)
else:
    print("yor failed",total_percntage)