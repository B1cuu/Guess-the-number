import random

randomNumber = random.randint(0, 100)
print("Guess the number from 0 to 100")

while True:
    guess = int(input("Enter your number suggestion: "))
    print(guess)

    if guess == randomNumber:
        break
    if guess > randomNumber:
        print("The given number is too large")
        continue
    if guess < randomNumber:
        print("The given number is too small")
        continue
print("Way to go! You managed to guess")