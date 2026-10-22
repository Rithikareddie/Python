users={
        1001:{'name':"Rithika",'gmail':"rithikareddyreethu@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"Rithwik",'gmail':"rithwikreddy@gmail.com",'balance':1000,'password':'1002'}
        }


# transfer function
def transfer(sender_account:int,receiver_account:int,transfer_amount:int):
    if receiver_account not in users:
        return "Receiver account does not exist"

    if users[sender_account]['balance'] >= transfer_amount:
        users[sender_account]['balance'] -= transfer_amount
        users[receiver_account]['balance'] += transfer_amount

        return f"{transfer_amount} transferred successfully to account {receiver_account} and\
                 current balance is :{users[sender_account]['balance']}"

    return "Insufficient Amount"