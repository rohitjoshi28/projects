account = {}

account_count =0

def create():
    global account_count
    account_holder_name = input("Enter Name:")
    initial_deposit = int(input("Enter Initial Amount:"))

    account_count += 1

    account[account_count] = {
        "name": account_holder_name,
        "balance": initial_deposit
    }
    print("Account created! Number:",account_count)

def deposit():
    account_number = int(input("Enter Acount Number: "))
    new_deposit = int(input("Enter Amount: "))

    account[account_number]["balance"] += new_deposit

    print("Deposited!")

def withdraw():
    account_number = int(input("Enter Acount Number: "))
    amt_withdeaw = int(input("Enter Amount: "))

    if amt_withdeaw <= account[account_number]["balance"]:
        account[account_number]["balance"] -= amt_withdeaw
        print("Withdrawn!")
    else:
        print("Not Enough Money")

def check():
    account_number = int(input("Enter Acount Number: "))

    print("Balance", account[account_number]["balance"])

while True:
    print("=================================")
    print("          Rohit's Bank              ")
    print("=================================")
    print("\n1. Create\n2. Deposit\n3. Withdraw\n4. Check\n5. Exit")

    choice = int(input("Choice: "))

    if choice == 1:
        create()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check()
    elif choice == 5:
        break

