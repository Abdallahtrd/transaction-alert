def user_balance():  #This function collects the balance input from the user.
    balance = int(input("Input Balance Please: "))
    return balance

def transaction_amount(): #This function collects the amount input from the user.
    amount = int(input("Please Input Transaction Amount: "))
    return amount

def transaction_type(): #This function allows for transaction type, Deposit/Withdraw.
    choice = input("Do you want to withdraw or deposit? ")
    if choice == "withdraw":
        print("User choice withdraw.")      
    elif choice == "deposit":
        print("User choice deposit.")
    else:
        print("Invalid choice")
    return choice                     

def des_withdraw(amount, balance): #This function calculates for Withdrawal.
    new_balance = balance - amount
    return new_balance    
     

def des_deposit(amount, balance): #This function calculates for Deposit.
    new_balance = balance + amount
    return new_balance

def main(): #This is the main function, This is where all the logic is carried out.

#This stores the values from previous functions in variables.    
    total_balance = user_balance()
    withdrawal_type = transaction_type()
    total_amount = transaction_amount()
     

#This is where the transaction type is processed.
    if withdrawal_type == "withdraw":
        new_balance = des_withdraw(total_amount, total_balance)
    elif withdrawal_type == "deposit":
        new_balance = des_deposit(total_amount, total_balance)
    else:
        print("INVALID REQUEST PLEASE TRY AGAIN")
        return new_balance
    print("Your balance is ", new_balance)
        
main()


    



