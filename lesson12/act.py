while True:
    print("#####power calculator#####")
    entry = input("enter a number (or type quit if u are done): ")
    if entry.lower() == "quit":
        print("goodbye")
        break
    number = int(entry)
    print("You entered:", number)
    exponent = int(input("Enter an exponent: "))
    print("You entered:", exponent)
    answer = number ** exponent
    print("output:", answer)