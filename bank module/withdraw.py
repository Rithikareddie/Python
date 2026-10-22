users={
        1001:{'name':"Rithika",'gmail':"rithikareddyreethu@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"Rithwik",'gmail':"rithwikreddy@gmail.com",'balance':1000,'password':'1002'}
        }


# withdraw function
def withdraw(account:int,withdraw_amount:int)-> str:
    curr_balance = users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdraw successful and\
                         current balance is :{users[account]['balance']}"
    return "Insufficient Amount"