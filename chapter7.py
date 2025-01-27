#WAP to print multiplication table using for loop
"""a = int(input("enter the number: "))
for i in range (1,11):
    print(f"{a} x {i} = {a * i}")"""

#WAP to greet people whose name starts with "S" ["ayush", "avi", "daksh", "swarnima", "saala"]
"""l = ["ayush", "avi", "daksh", "swarnima", "saala"]
for name in l:
    if(name.startswith("s")):
        print(f"hello bruh {name}")"""
#attempt problem 1 by while loop
"""a = int(input("enter the number: "))
i = 1
while(i < 11):
    print(f"{a} x {i} = {a *i}")
    i += 1"""

#WAP to find wether the given number is prime or not 
"""a = int(input("enter the number : "))
for i in range(2, a):
    if (a%i) ==  0:
        print("the number is not prime ")
    else:
        print("the number is prime")"""

#WAP to find the sum of first n natural numbers using while loop 
"""n = int(input("enter the number: "))
i = 0 
sum = 0 
while(i <= n):
    sum += i
    i += 1
print(sum)"""

#WAP to find a factorial of a given number using for loop 
a = int(input("enter the number: "))
product = 1
for i in range (1, a+1):
    product = product*i
print(product)
