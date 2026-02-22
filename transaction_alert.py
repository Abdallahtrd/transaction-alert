def user_balance():  #This function collects the balance input from the user and makes sure its the correct input.
    while True:
        try:
            balance = int(input("Input Balance Please: "))
            break
        except:
            print("Invalid input!! Please Input Balance.")
    return balance

def transaction_amount(): #This function collects the amount input from the user and makes sure its the correct input.
    while True:
        try:
            amount = int(input("Please Input Transaction Amount: "))
            break
        except:
            print("Invalid input!!  Please Input a Amount.")
    return amount

def transaction_type(): #This function allows for transaction type, Deposit/Withdraw.
    choice = input("Do you want to withdraw or deposit? use w/d ").lower()
    if choice == "w":
        print("User choice withdraw.")     
    elif choice == "d":
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

def main(balance): #This is the main function, This is where all the logic is carried out.

#This stores the values from previous functions in variables.    
#Balance is now managed at loop scope instead of inside main.
    withdrawal_type = transaction_type()
    total_amount = transaction_amount()
    

     
#This is where the transaction type is processed.
    if withdrawal_type == "w":
        new_balance = des_withdraw(total_amount, balance)
    elif withdrawal_type == "d":
        new_balance = des_deposit(total_amount, balance)
    else:
        print("INVALID REQUEST PLEASE TRY AGAIN")
        return balance #This returns the unchanged balance if the user gives a wrong input.
    print("Your balance is ", new_balance)
    return new_balance #This returns the calculated balance to where the main function is called.
        

balance = user_balance() #This collects the user input once before the loop starts.

while True: #This is the part that makes the whole program repeatable.
    run_choice = input("Do you want to run a transaction? yes/no ").lower()
    if run_choice == "yes":
        balance = main(balance)
    elif run_choice == "no":
        print("Thank you for using T-Pay!! ")
        break
    else:
        print("Invalid Input!! Try again. ")
        break

