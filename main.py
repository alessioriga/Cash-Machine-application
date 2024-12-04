# datetime module is imported to get the date, which will be used to indicate when a transaction is made
import datetime
# time module adds a delay in seconds between each string (where it has been added "time.sleep()")
import time


# I created a dictionary that contains two dictionaries with the account information
atm = {
    "account_1": {
        "pin": 1234,
        "balance": 5000,
        "t_history": []
    },
    "account_2": {
        "pin": 4321,
        "balance": 7000,
        "t_history": []
    }
}

# This function starts the program and initiates the authentication procedure
def atm_startup():
    print("~ Welcome to the KRAL ATM ~")
    time.sleep(1)
    account = validation_pin()
    atm_menu(account)

def validation_pin():
    # This function takes the pin and checks if it is correct
    while True:
        try:
            pin = int(input("\nEnter your PIN: "))
            for account, values in atm.items():
                # If the entered pin is in items of atm dictionary,
                # it returns the matching account key
                if values["pin"] == pin:
                    print("\nAccess GRANTED!")
                    time.sleep(1)
                    return account
                 
            print("\nInvalid PIN. Please Try again.")
        except ValueError:
            # If a ValueError occurs, the program will not show an error but will display the following message,
            # letting the user know that only numbers are allowed
            print("\nInvalid input. Only numbers allowed. Please try again.")

def atm_menu(account):
    # Once access has been granted, the program sends the account number to the ATM menu so the user can navigate their account's menu
    print("Welcome back.")
    time.sleep(1)
    while True:
        print("\nWhat would you like to do?")
        print("1: Check my BALANCE")
        print("2: WITHDRAW Cash")
        print("3: Make a DEPOSIT")
        print("4: Check TRANSACTION HISTORY")
        print("5: EXIT")

        choice = input("\nSelect a service (1 - 5): ")
        # Option 1 lets the user check their account balance
        if choice == '1':
            check_balance(account)
        # Option 2 allows the user to withdraw money from their bank account
        if choice == '2':
            withdraw_money(account)
        # Option 3 lets the user deposit money into their account
        if choice == '3':
            deposit_money(account)
        # Option 4 lets the user check their recent transactions
        if choice == '4':
            check_transaction_history(account)
        # Option 5 allows the user to exit their bank account
        if choice == '5':
            print("\nThank you for using KRAL ATM.")
            break
        # The program accepts only numbers between 1 and 5.
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1)

def check_balance(account):
    # This function displays the current balance of the user
    balance = atm[account]["balance"]
    print(f"\nYour current balance is: £{balance:.2f}")
    time.sleep(1)

def withdraw_money(account):
    while True:
        try:
            amount = float(input("\nEnter the amount to withdraw: £"))
            balance = atm[account]["balance"]

            if amount > balance:
                # If the user wants to withdraw more money than they have in the account
                print(f"\nInsufficient funds for this transaction. Available balance: £{balance:.2f}")
                print("Please try again.")
            if amount <= balance:
                date = datetime.datetime.now()
                atm[account]["balance"] -= amount
                # The following string will append the transaction to the history with the date and time it was made
                atm[account]["t_history"].append(f"{date.strftime('%d-%m-%y %H:%M:%S')} Withdrawn: £{amount:.2f}")
                print(f"\nYou have withdrawn £{amount:.2f}")
                time.sleep(1)
                break
        except ValueError:
            # If a ValueError occurs, the program will not show an error but will display the following message,
            # letting the user know that only numbers are allowed
            print("\nInvalid input. Only numbers are allowed. Please try again.")

def deposit_money(account):
    while True:
        try:
            amount = float(input("\nEnter the amount to deposit: £"))
            
            if amount > 0:
                date = datetime.datetime.now()
                atm[account]["balance"] += amount
                # The following string will append the transaction to the history with the date and time it was made
                atm[account]["t_history"].append(f"{date.strftime('%d-%m-%y %H:%M:%S')} Deposited: £{amount:.2f}")
                print(f"\nYou have deposited £{amount:.2f}")
                time.sleep(1)
                break
            else:
                print("\nInvalid deposit amount. Please enter a positive value.")
        except ValueError:
            # If a ValueError occurs, the program will not show an error but will display the following message,
            # letting the user know that only numbers are allowed
            print("\nInvalid input. Only numbers are allowed. Please try again.")

def check_transaction_history(account):
    if atm[account]["t_history"]:
        print("\nTransaction History:")
        # This function prints all the transactions that the user has made 
        for transaction in atm[account]["t_history"]:
            print(transaction)
            time.sleep(1)
    else:
        # If there are no transactions in the history, the following message will be shown
        print("\nNo transactions have been made yet.")
        time.sleep(1)

# This function starts the program
atm_startup()
