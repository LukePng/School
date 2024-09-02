"""
#3A
def health():
    age = int(input("Enter your age: "))
    BMI = float(input("Enter your BMI: "))
    if age < 45 and BMI < 22.0:
        print("Low")
    elif age < 45 and BMI >= 22.0:
        print("Medium")
    elif age >= 45 and BMI < 22.0:
        print("Medium")
    else:
        print("High")
health()

def rock_paper_scissors():
    quit = False
    while not quit:
        p1 = input("Enter R S or P: ")
        p2 = input("Enter R S or P: ")
        if p1 == p2:
            print("Draw")
        elif p1 == "R" and p2 == "S":
            print("Player 1 wins")
        elif p1 == "S" and p2 == "P":
            print("Player 1 wins")
        elif p1 == "P" and p2 == "R":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        quit = (input("Do you want to quit? (y/n) ") == "y")
rock_paper_scissors()
        
#3B
for i in range(1, 129):
    print(f"{chr(i)}: {i}")


testString = "Hello World"
def printASCII(testString):
    for i in testString:
        print(f"{i}: {ord(i)}")

def spaceCounter(testString):
    counter = 0
    for i in string:
        if i == " ":
            counter += 1
    print(f"space counter: {counter}")
printASCII(testString)
spaceCounter(testString)

def find_pi():
    approx = int(input("Enter the number of terms: "))
    pi = 0
        for n in range(1,iterations+1):
            pi += -4 * (-1)**n / (2*n-1)
    print(pi)
find_pi()

def ave_temp():
    noon_temp = list(input("Enter a list of temperatures at noon: "))
    ave = 0
    days = 0
    for i in noon_temp:
        if i >= 0:
            ave += i
            days += 1
    ave /= days
    print(f"The average temperature is {ave:.2f}")
ave_temp()
"""
num = int(input("Enter the number of rows: "))
max_len = len(str(num*num))
print(" "*(max_len+1), end='')
for i in range(1,num+1):
    print(f"{i:<{max_len+1}}", end='') #Prints first row
print()

for i in range(1,num+1):
    print(f"{i:<{max_len}}", end=" ") #Prints first column
    for j in range(1,i+1):
        print(f"{i*j:<{max_len}}",end=' ') #Prints the rest of the row
    print()

"""
#3C
p_sum = 0
while True:
    item = input("enter item name or xyz to stop: ")
    if item == "xyz":
        break
    else:
        price = float(input("enter price per item"))
        quantity = int(input("enter quantity: "))
        print(f"{str(quantity)+' '+item:20}$ {price*quantity:,.2f}")
        p_sum += price*quantity
print(f"{'Total Bill':20}$ {p_sum:,.2f}")

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
if num1 > num2:
    largest = num1
    smallest = num2
else:
    largest = num2
    smallest = num1
    

while smallest != 0:
    remainder = largest % smallest
    largest = smallest
    smallest = remainder
print(largest)
"""
