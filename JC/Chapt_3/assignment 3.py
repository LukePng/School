"""
def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
print(factorial(5))

def check_word(word):
    vowels = ['a','e','i','o','u']
    num_vowels = 0
    for letter in word:
        if letter in vowels:
            num_vowels += 1
    print(f"Letters: {len(word)}")
    print(f"Vowels: {num_vowels}")
    print(f"Percentage of vowels: {num_vowels/len(word):.2%}")

check_word("hello")

def rectangle(n):
    print("* " * (2*n))
    for _ in range(n-2):
        print("* " + "  "*(2*n-2) + "* ")
    print("* " * (2*n))
    
rectangle(5)

import random

def gamble():
    max_amt = 0
    rolls = 0
    money = int(input("Enter starting amt: "))
    while money != 0:
        rolls += 1
        if random.randint(1,7) + random.randint(1,7) == 7:
            money += 4
        else:
            money -= 1
        max_amt = max(money,max_amt)
    print(f"{rolls = }\n{max_amt = }")
gamble()

def user_guess():
    ans = random.randint(1,100)
    tries = 0
    while True:
        guess = int(input("Enter a guess"))
        if guess != ans:
            print("Too small" if guess < ans else "Too large")
            tries += 1
        else:
            print(f"you got it in {tries} tries!")
            break
user_guess()

def comp_guess():
    ans = max(min(int(input("Enter a number between 0-100")),100),0)
    tries = 0
    while True:
        guess = random.randint(1,100)
        print(f"guessing {guess}")
        if guess != ans:
            tries += 1
        else:
            print(f"solved in {tries} tries!")
            break
comp_guess()
"""
