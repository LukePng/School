amount = 24.325
print (f"Your salary is ${amount:.2f}")
print (f"The area is {amount:.1f}")
print (f"{amount:7f}")
print (f"BMI btw {18.5:f} and {amount:2.3f} is ideal")
print (f"Overweight ={amount:>7.2f} - {29.9:.2f}")

x, y, z = 1, 23, 456
print(f"{x:>6} {y:>6} {z:>6}")

from math import pow, pi 
print(pow(8, 2))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old, in ten years you are {age + 10} years old")

radius = float(input("Enter the radius of the circle: "))
diameter = 2 * radius
circumference = 2 * pi * radius
volume = 4/3 * pi * radius ** 3
area = 4 * pi * radius ** 2
print(f"Diameter: {diameter:.2f}, Circumference: {circumference:.2f}, Volume: {volume:.2f}, Area: {area:.2f}")

wage = int(input("Enter your wage: "))
hours = int(input("Enter the number of hours worked: "))
overtime = int(input("Enter the number of overtime hours worked: "))
total = wage * hours + 1.5 * wage * overtime
print(f"Your total wage is {total:.0f}")

bought_old = int(input("Enter the number of day old bread bought: "))
bought_new = int(input("Enter the number of fresh bread bought: "))  
print(f"Price of fresh bread: ${bought_new * 3.50:.2f}\nPrice of day old bread: ${bought_old * 3.50 * 60/100:.2f}\nTotal cost: ${bought_old * 3.50 * 60/100 + bought_new * 3.50:.2f}")




