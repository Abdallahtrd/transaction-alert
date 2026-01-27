balance = 10000
 

def transaction_amount():
    name = input("What is your name sir? ")
    amount = int(input("How much would you like to withdraw: "))
    total = balance - amount
    print(name, total)
transaction_amount()
    