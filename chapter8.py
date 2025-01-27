#functions and recursion
"""def goodDay(name):
    print("hello," + name)
goodDay("ayush")"""
"""#WAP to find geratest pf three numbers
# Program to find the greatest of three numbers
# Input values
a = 1  # First number
b = 10  # Second number
c = 20  # Third number

# Function to determine the largest number
def large(a, b, c):  # Defining a function named 'large' that takes three parameters
    if a > b and a > c:  # Check if 'a' is greater than both 'b' and 'c'
        return a  # Return 'a' as the largest number
    elif b > a and b > c:  # Check if 'b' is greater than both 'a' and 'c'
        return b  # Return 'b' as the largest number
    else:  # If both conditions above are false, 'c' is the largest
        return c  # Return 'c' as the largest number

# Print the result by calling the function with the given inputs
print("The largest number is:", large(a, b, c))"""

#WAP convert celsius to fehranite using def
# Program to convert Celsius to Fahrenheit

# Input temperature in Celsius
"""c = float(input("Enter the temperature in Celsius: "))

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32  # Formula to convert Celsius to Fahrenheit

# Print the converted temperature
print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))"""

#write a recursive finction to to print the sum of n natural numbers
"""def sum(n):
    if(n==1):
        return 1
    return sum(n -1) + n
print(sum(5))"""

#WAP to convert inches into cm

"""def inch_to_cm(x):
    return x * 2.25
x = float(input("enter the value in inches: "))
print(f"this is conersion{inch_to_cm(x)}")"""

#WAP to remove a word from given list and strip at the same time


l = ["ayush", "manav", "daksh", "chicken"] #created a list 

"""def rem(l, word): # defined a function named rem
    for item in l: #using for loop 
        l.remove(word) #  .remove function for removing items from the list(open bracket mei humnei wod naam ka variable likha hai aur bd mie ja kr print comment sei vo string select krenge jo remove krin hogi ) 
        return l #puri list retuen kre ga 
print(rem(l, "chicken"))   #chicken  word humko remove  krna hai issiliiyea humnei chicken likhdiyea"""
#WAP for multiplication table using def function
"""def multiplication(n):
    for i in range (1,11):
        print(f"{n} X {i} = {n*i}")
multiplication(5)"""