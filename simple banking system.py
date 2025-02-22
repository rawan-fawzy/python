balance = 1000 

while True:
    print("\nWelcome to Simple Bank System!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"Your balance is {balance}")
    elif choice == '2':
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"Deposit successful! Your balance is {balance}")
        else:
            print("Invalid deposit amount")
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful! Your balance is {balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount")
    elif choice == '4':
        print("Thank you for using Simple Bank System!")
        break
    else:
        print("Invalid choice. Please try again.")
