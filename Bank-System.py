# Banking System
# This a banking system where users can deposit, withdraw, and check their balance.
# It also includes account number and PIN validation.

# The user must enter a valid account number and PIN before continuing.
def get_valid_account_number():
    while True:
        account_number = input("Enter your 10-digit Account number: ")
        if not account_number.isnumeric():  # Check if account number contains digits only
            print("Invalid Account Number! It must contain digits only. TRY AGAIN!")
            continue
        if len(account_number) != 10:  # Check if account number is exactly 10 digits
            print("Account number must be exactly 10 digits! TRY AGAIN!")
            continue
        return account_number

def get_valid_pin():
    while True:
        pin = input("Enter your 4-digit PIN: ")
        if not pin.isdigit():  # Check if PIN contains digits only
            print("Invalid PIN! It must contain digits only. TRY AGAIN!")
            continue
        if len(pin) != 4:  # Check if PIN is 4 digits only
            print("PIN must be exactly 4 digits! TRY AGAIN!")
            continue
        return pin
    
# Get valid account number and PIN
account_number = get_valid_account_number()
print(f"Account number: {account_number} is valid.")
pin = get_valid_pin()  
print("PIN is valid.")

Amount = 0  # Initialize amount

while True:
    print("\n--- Banking System Menu ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. View Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":  # Deposit Money
        while True:
            deposit_amount = input("Enter amount to deposit: ")
            if not deposit_amount.isnumeric():
                print("Invalid Amount! Amount must contain digits only. TRY AGAIN!")
                continue
            deposit_amount = int(deposit_amount)
            if deposit_amount <= 0:
                print("Amount must be greater than zero! TRY AGAIN!")
                continue
            Amount += deposit_amount
            print(f"Amount deposited: R{deposit_amount}. \n Current balance: R{Amount}.")
            break

    elif choice == "2":  # Withdraw Money
        while True:
            withdrawal_amount = input("Enter amount to withdraw: ")
            if not withdrawal_amount.isnumeric():
                print("Invalid Amount! Amount must contain digits only. TRY AGAIN!")
                continue
            withdrawal_amount = int(withdrawal_amount)
            if withdrawal_amount <= 0:
                print("Withdrawal amount must be greater than zero! TRY AGAIN!")
                continue
            if withdrawal_amount > Amount:
                print("Insufficient funds! Cannot withdraw more than the current balance.")
                continue
            Amount -= withdrawal_amount
            print(f"Amount withdrawn: R{withdrawal_amount}. \n Remaining balance: R{Amount}.")
            break

    elif choice == "3":  # View Balance
        print(f"Your current balance is: R{Amount}.")

    elif choice == "4":  # Exit
        print("Thank you for using the Banking System. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option (1-4).")

# End of Banking System
#886356