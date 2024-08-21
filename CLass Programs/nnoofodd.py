a=int(input("Enter the number:-"))
sum_of_odd=0
for i in range(1,a+1,2):
    sum_of_odd+=i
    
print("The sum of odd numbers up to", a, "is:", sum_of_odd)