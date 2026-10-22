# DATA BASE

# Import requirements
from emailsend import singleEmailSend


users = {
    1001: {
        'name': "Rithika",
        'email': "ritikareddyreethu@gmail.com",
        'balance': 5000,
        'password': '1001'
    },

    1002: {
        'name': "Prasanna",
        'email': "mutyalaprasannareddy@gmail.com",
        'balance': 4000,
        'password': '1002'
    }
}


# Register function
def register(username: str, email: str, balance: int, password: str) -> str:
    return "Register page under development process"


# Login Function
def login(account: int, password: str) -> bool:
    if account in users:
        if users[account]['password'] == password:
            return True
        return False
    return False


# Get Balance
def balance(account: int) -> str:
    curr_balance = users[account]['balance']
    return f"Current Balance is: {curr_balance}"


# Withdraw
def withdraw(account: int, withdraw_amount: int) -> str:
    curr_balance = users[account]['balance']

    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount

        singleEmailSend(
            to_email=users[account]['email'],
            subject="Withdraw Alert",
            body=f"{withdraw_amount} withdraw successful and current balance is: {users[account]['balance']}"
        )

        return f"{withdraw_amount} withdraw successful and current balance is: {users[account]['balance']}"

    return "Insufficient Amount"


# Deposit Function
def deposit(account: int, deposit_amount: int) -> str:
    users[account]['balance'] += deposit_amount

    return f"{deposit_amount} Deposit successful and current balance is: {users[account]['balance']}"


# Transfer Function
def transfer(from_acc: int, to_acc: int, transfer_amount: int):
    if to_acc not in users:
        return "Receiver account does not exist"

    if users[from_acc]['balance'] >= transfer_amount:
        users[from_acc]['balance'] -= transfer_amount
        users[to_acc]['balance'] += transfer_amount

        return f"{transfer_amount} transferred successfully"

    return "Insufficient balance"


# Mini Statement Function
def ministatement(account: int):
    print("Mini statement page")


# Logout Function
def logout():
    print("Bye Bye Buddy, see you later")


# Main
if __name__ == "__main__":

    print("Welcome to the Mini Bank")
    print("1. Login")
    print("2. Register")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        # Call login function
        account = int(input("Enter Your Account Number: "))
        password = input("Enter Your Password: ")

        login_val = login(account=account, password=password)

        if login_val:

            while login_val:

                print("\n1. Get Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Mini Statement")
                print("6. Logout")

                choice = int(input("Enter your choice: "))

                if choice == 1:

                    print(balance(account=account))

                elif choice == 2:

                    amount = int(input("Enter withdraw amount: "))

                    print(
                        withdraw(
                            account=account,
                            withdraw_amount=amount
                        )
                    )

                elif choice == 3:

                    amount = int(input("Enter Deposit amount: "))

                    print(
                        deposit(
                            account=account,
                            deposit_amount=amount
                        )
                    )

                elif choice == 4:

                    receiver = int(input("Enter receiver account number: "))
                    amount = int(input("Enter Transfer amount: "))

                    print(
                        transfer(
                            from_acc=account,
                            to_acc=receiver,
                            transfer_amount=amount
                        )
                    )

                elif choice == 5:

                    print(ministatement(account=account))

                elif choice == 6:

                    logout()
                    login_val = False

                else:

                    print("Select your choice between 1-6")

        else:

            print("Invalid Login credentials")

    elif choice == 2:

        username = input("Enter user name: ")
        email = input("Enter user email id: ")
        initial_deposit = int(input("Enter the initial Deposit amount: "))
        password = input("Enter your new password: ")

        print(
            register(
                username=username,
                email=email,
                balance=initial_deposit,
                password=password
            )
        )

    else:

        print("Invalid choice, please select 1 or 2")
