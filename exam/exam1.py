import random
num = random.randint(1, 50)
print("number guessing game")
guess=int(input("enter a number between 1 to 50:       "))
attempts=3
while True:
 if guess == num:
    print("well done,congrats")
    break
 elif guess != num:
    attempts -= 1
    print (f" incorrect,u have {attempts} left ")
    if attempts == 0:
        print(f"ooff, better luck next time kiddo, btw the number was {num}")
        break
    guess = int(input("enter a number between 1 to 50:       "))