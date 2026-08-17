import random
num = random.randint(1, 50)
print("number guessing game")
guess=int(input("enter a number between 1 to 50:       "))
attempts=5
while True:
 if guess == num:
    print("well done,congrats")
 elif:
    attempts - 1
    print (f" incorrect,u have {attempts} left ")
 else:
   attempts==0
   print(f"ooff, better luck next time kiddo, btw the number was {num}")