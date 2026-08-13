print("########################################################################")
print("                        ATM cash deposition app                         ")
print("########################################################################")


while True:
    name = input("enter ur name: ")
    amount = int(input("enter the amount u want to withdraw: "))

    if amount <= 0:
        print("invalid amount")
    else:
        print(f"giving the {amount} to {name}")

        rem = amount
        i = 1
        while i <= 6:
            if i == 1:
                value = 100
            elif i == 2:
                value = 50
            elif i == 3:
                value = 20
            elif i == 4:
                value = 10
            elif i == 5:
                value = 5
            elif i == 6:
                value = 1

            print(f"denomination {i}: {value}")
            rem -= value
            i += 1

            withdraw = input("Do you want another transaction? (yes/no): ")
    if withdraw.lower() == "yes":
        continue
    else:
        break
