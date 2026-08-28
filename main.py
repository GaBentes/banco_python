import os

menu = f"""{"#"*30} Bank Name {"#"*30}
[d] Deposit
[w] Withdraw
[h] History
[q] Quit

=> """

balance = 0
limit = 500.0
WITHDRAW_LIMITS = 3
deposits = []
withdraws = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    option = input(menu)

    if option.lower() == "d":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{"#"*30} Deposit Page {"#"*30}")
        while True:
            deposit = input("Enter an amount to deposit or press [q] to quit\n=> ")            
            
            if deposit.lower() == 'q':
                break
            
            deposit = float(deposit)          
                        
            if deposit <= 0: 
                    print("Error: The deposit must be greater than 0")
            else:
                balance += deposit
                deposits.append(deposit)
                break
            

    elif option.lower() == "w":
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print(f"{"#"*30} Withdraw Page {"#"*30}")
            print(f"Your balance: ${balance:.2f}")
            withdraw = input("Enter the amount to withdraw or press [q] to quit\n=> ")

            if withdraw.lower() == 'q':
                break
                
            withdraw = float(withdraw)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            if balance <= 0:                
                print("ERROR: There is no money available to withdraw")
                option = input("Press [q] to quit\n=> ")
                if option == 'q':
                    break
            elif withdraw > balance: 
                print("ERROR: Insufficient funds")
                # break
            elif withdraw <= 0:
                print("ERROR: The withdraw value must be greater than 0")
            elif withdraw > limit:
                print(f"WARNING: The maximum withdraw amount is ${limit:.2f}\nPlease enter a lower amount")
            elif WITHDRAW_LIMITS == 0:
                print("WARNING: You have reached the daily withdrawal limit of 3 transactions\nYou cannot make another withdrawal today")
                break
            else:
                balance -= withdraw
                WITHDRAW_LIMITS -= 1
                withdraws.append(withdraw)
                break


    elif option.lower() == "h":
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{"#"*30} Account Statement {"#"*30}")

            print("Deposit History:")
            if not deposits:
                print("None")
            else:
                for indice, d in enumerate(deposits):
                    print(f"Deposit number: {indice + 1} - ${d:.2f}")

            print("\nWithdraw History:")
            if not withdraws:
                print("None")
            else:
                for indice, w in enumerate(withdraws):
                    print(f"Extract number: {indice + 1} - ${w:.2f}")
            print(f"\nFinal balance for the day: ${balance:.2f}")                    

            print("\nPress [q] on your keyboard to quit")
            option = input("=>")
            if option.lower() == 'q':
                break


    elif option.lower() == "q":
        print("Quitting...")
        break
    else:
        print("input mismatch. Please try again")