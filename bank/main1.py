#Data base
"""
users={
        Account:{
            'name':Username,
            'email':user email,
            'balance':5000,
            'password':password
            }
        }
"""
users={
        1001:{
            'name':'Rithika','email':'ritikareddyreethu@gmail.com','balance':5000,'password':'1001'},
        1002:{
            'name':'Prasanna','email':'mutyalaprasannareddy@gmail.com','balance':4000,"password":'1002'}, 
      }
#Register function
def register(username:str,email:str,balance:int,password:str)->str:
    print("User in register page")
    return "Register page under development process"

#Login function 
def login(account:int,password:str)->bool:
    print("User in login page")
    if account in users:
        if users[account]['password']==password:
            return True
        return False
    return False

#get current balance function
def balance(account:int)->str:
    print("User in balance page")
    curr_balance=users[account]['balance']
    return f"Current Balance is:{curr_balance}"

#withdraw function
def withdraw(account:int,withdraw_amount:int)->str:
    print("User in withdraw page")
    curr_balance=users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdraw successful and current balance is :{users[account]['balance']}"
    return "Insufficient Amount"

#deposit
def deposit(account:int,deposit_amount:int)->str:
    print("User in deposit page")
    users[account]['balance']+=deposit_amount
    return f"{deposit_amount} deposit successful and current balance is :{users[account]['balance']}"
#transfer
def transfer(from_acc:int,to_acc:int,transfer_amount:int):
    print("User in transfer page")
    curr_balance=users[from_acc]['balance']
    if curr_balance >= transfer_amount:
        users[from_acc]['balance']-= transfer_amount
        users[to_acc]['balance'] += transfer_amount
        return f"{transfer_amount} Transfer Successful and Current Balance is:{users[from_acc]['balance']}"
    return "Insufficient Amount"
    
#get mini statement
def ministatement(account:int):
    print("User in Ministatement page")
    return "Ministatement page under development process"
#logout
def logout():
    print("Bye Bye buddy,see you later")
    exit()

#main
if __name__=="__main__":
    print("Welcome to the Mini Bank")
    print("1.Login \n 2.Register")
    choice=int(input("Enter your choice:"))
    if choice==1:
        #Call Login
        account=int(input("Enter your account number:"))
        password=input("Enter your password:")
        login_val=login(account=account,password=password)
        while login_val:
            print("1.Get Balance\n 2.Withdraw \n 3.Deposit \n 4.Transfer \n 5.MiniStatement \n 6.Logout")
            choice=int(input("Enter your choice:"))
            if choice==1:
                #Call Balance functions
                print(balance(account=account))
            elif choice==2:
                amount=int(input("Enter Withdraw Amount:"))
                print(withdraw(account=account,withdraw_amount=amount))
            elif choice ==3:
                amount=int(input("Enter Deposit Amount:"))
                print(deposit(account=account,deposit_amount=amount))
            elif choice==4:
                receiver=int(input("Enter receiver account number:"))
                amount=int(input("Enter Deposit Amount:"))
                print(transfer(from_acc=account,to_acc=receiver,transfer_amount=amount))
            elif choice==5:
                print(ministatement(account=account))
            elif choice==6:
                print(logout())
            else:
                print("Select your choice in between 1-6")
        else:
            print("Invalid Login Credentials")
    elif choice==2:
        #call register
        username=input("Enter Username:")
        email=input("Enter User email id:")
        initial_deposit=int(input("Enter initial deposit amount:"))
        password=input("Enter your new password:")
        register_val=register(username=username,email=email,balance=initial_deposit,password=password)
    else:
        print("Invalid choice,Please select 1 or 2")