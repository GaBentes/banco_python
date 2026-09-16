import textwrap
from os import system, name
from time import sleep


def clean_screen():
    system("cls" if name == "nt" else "clear")


def menu():
    menu = f"""{"#"*30} Bank Name {"#"*30}
[d] Deposit
[w] Withdraw
[h] History
[nu] New User
[ra] Register Account
[lc] List accounts
[q] Quit

=> """
    return input(textwrap.dedent(menu))


def deposit(value, deposits, balance):
    while True:
        if value.lower() == "q":
            break

        value = float(value)

        if value <= 0:
            print("Error: The deposit must be greater than 0")
        else:
            balance += value
            deposits.append(value)
            print(balance)
            return balance


def withdraw(value, withdraws, balance, limit, WITHDRAW_LIMITS):
    while True:
        clean_screen()
        if value.lower() == "q":
            break
        value = float(value)
        if balance <= 0:
            print("ERROR: There is no money available to withdraw")
            # option = input("Press [q] to quit\n=> ")
            # if option == "q":
            #     break
        elif value > balance:
            print("ERROR: Insufficient funds")
            # break
        elif value <= 0:
            print("ERROR: The withdraw value must be greater than 0")
        elif value > limit:
            print(
                f"WARNING: The maximum withdraw amount is ${limit:.2f}\nPlease enter a lower amount"
            )
        elif WITHDRAW_LIMITS == 0:
            print(
                "WARNING: You have reached the daily withdrawal limit of 3 transactions\nYou cannot make another withdrawal today"
            )
            break
        else:
            balance -= value
            WITHDRAW_LIMITS -= 1
            withdraws.append(value)
            break
        value = input("\nEnter another amount or press [q] to quit\n=> ")
    return balance, WITHDRAW_LIMITS


def history(deposits, withdraws, balance):
    while True:
        clean_screen()
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
        if option.lower() == "q":
            break


def register_user(users):
    while True:
        clean_screen()
        print(f"{"#"*30} Register User {"#"*30}")
        name = input("First name: ")
        surname = input("Surname: ")
        date_of_birth = input("Enter your complete date of birth (month-day-year): ")
        cpf = input("Cpf: ")
        cpf_already_in_use = any(user["cpf"] == cpf for user in users)
        if cpf_already_in_use:
            print("Cpf already in use")
            option = input("Press [q] to quit: ")
            if option.lower() == "q":
                break
        else:
            address = input("Please state your complete address: ")
            users.append(
                {
                    "name": name,
                    "surname": surname,
                    "date_of_birth": date_of_birth,
                    "cpf": cpf,
                    "address": address,
                }
            )
            print("User successfully created!")
            print("Quitting...")
            sleep(2)
            break


def register_account(users, accounts):
    while True:
        clean_screen()
        print(f"{'#'*30} Register Account {'#'*30}")
        cpf = input("Type your cpf: ")

        user_found = None
        for user in users:
            if user["cpf"] == cpf:
                user_found = user
                break

        if user_found:
            account_number = len(accounts) + 1

            full_name = f"{user_found['name']} {user_found['surname']}"

            accounts.append(
                {
                    "agency": "0001",
                    "account": account_number,
                    "user": full_name,
                    "cpf": cpf,
                }
            )
            print("Account successfully created!")
            print("Quitting...")
            sleep(2)
            break
        else:
            print("Error: User not found. Please register the user first.")
            option = input("Press [q] to quit or enter to try again: ")
            if option.lower() == "q":
                break


def list_accounts(accounts):
    while True:
        clean_screen()
        print(f"{'#'*30} List of Accounts {'#'*30}")

        if not accounts:
            print("Nenhuma conta cadastrada ainda.")
        else:
            for account in accounts:
                agency = account["agency"]
                acc_num = account["account"]
                user = account["user"]

                print("-" * 120)
                print(f"Agency: {agency} | Account: {acc_num} | Owner CPF: {user}")
                print("-" * 120)

        print("\nPress [q] on your keyboard to quit")
        option = input("=> ")
        if option.lower() == "q":
            break


def main():
    value = 0
    balance = 0
    limit = 500.0
    WITHDRAW_LIMITS = 3
    users = []
    accounts = []
    deposits = []
    withdraws = []

    while True:
        clean_screen()
        opcao = menu()

        match opcao:
            case "q":
                break

            case "d":
                clean_screen()
                print(f"{"#"*30} Deposit Page {"#"*30}")
                value = input("Enter an amount to deposit or press [q] to quit\n=> ")
                balance = deposit(value, deposits, balance)

            case "w":
                clean_screen()
                print(f"{"#"*30} Withdraw Page {"#"*30}")
                print(f"Your balance: ${balance:.2f}")
                value = input("Enter the amount to withdraw or press [q] to quit\n=> ")
                balance, WITHDRAW_LIMITS = withdraw(
                    value, withdraws, balance, limit, WITHDRAW_LIMITS
                )

            case "h":
                history(deposits, withdraws, balance)

            case "nu":
                register_user(users)

            case "ra":
                register_account(users, accounts)

            case "lc":
                list_accounts(accounts)


main()
