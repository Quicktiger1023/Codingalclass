import random
number = random.randint(1, 10)

print("Welcome to the game here are the rules:\n" \
"1.think of a number between 1 to 10 \n" \
"2. the computer will try to guess the number u think \n " \
"3. there will be options that whether u ant to continue or quit.\n" \
"4. ALL THE BEST!!! \n")
name=input("Enter your name:       ")
print(f"welcome,{name}. Now think of a number between 1 to 10")

while True: 
    guess=input(f"is ur number {number}? (yes/no/quit):      ")
    
    if guess.lower() == "quit":
        print("goodbye")
        break
    elif guess.lower() == "no":
        print("okay lets try this again")
        number = random.randint(1, 10) 
        continue
    elif guess.lower() == "yes":
        print("well done!")

        choice = input("do u want to quit(to quit just type quit):      ")
        if choice.lower() == "quit":
            print("goodbye")
            break
        else:
            number = random.randint(1, 10) 
