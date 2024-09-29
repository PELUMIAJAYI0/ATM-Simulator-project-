def welcome():
    print("...Main Menu...")
    print("...Choose the following options...")
    print("1. Cash Withdrwal")
    print("2. Balance Inquiry")
    print("3. Funds Transfer")
    print("4. Bills Payment")
    print("5. Mini Statement")
    print("6. Other Options")

def cash_withdrawal():
    print("...Withdrawal of cash...")
    amount = int(input("Enter the amount to withdraw---> $"))
    if amount > 150000:
        print("Canot with draw money")
    else:
        print("Withdrawal of cash is successful")
        print("The ATM will dispense the cash")

def balance_inquiry():
    print("...Balnce Inquiry...")
    print("Your current balance is---> $100000")

def fund_transfer():
    print("...Fund Transfer...")
    destination = input("Choose the destination account type \n 1.Own Account \n 2. Other Account \n ---> ")
    if destination == "1":
        print("You have chosen to transfer money to your own account")
    elif destination == "2":
        print("You have chosen to transfer money to other account")
        acct_num = int(input("Enter the account number---> "))
        if len(acct_num) != 10:
            print("Enter a valid ten digit account number")
        else:
            amt = int(input("Enter the transfer amount---> $"))
            if amt > 150000:
                print("The amount is too high, please enter a lesser amount")
            else:
                print("The transfer is successful")

def bills_payemnt():
    print("...Bills Payment...")
    print("Choose the biller \n 1. Electricity \n 2. Water \n 3. Phone")
    biller = input(" ---> ")

    if biller == "1":
        print("You have chosen to pay electricity bill")
        elect = int(input("Enter meter number---> "))
        if elect.isdigit():
            elect_bill = int(input("Enter the amount to pay---> "))
            if elect_bill > 150000:
                print("The amount is too high, please enter a lesser amount")
            else:
                print("The payment is successful")
        else:
            print("Enter a valid meter number")

    elif biller == "2":
        print("You have chosen to pay water bill")
        water = int(input("Enter water number---> "))
        if water.isdigit():
            water = int(input("Enter the amount to pay---> "))
            if water > 150000:
                print("The amount is too high, please enter a lesser amount")
            else:
                print("The payment is successful")
        else:
            print("Enter a valid water number")
    
    elif biller == "3":
        print("You have chosen to pay phone bill")
        phone = int(input("Enter phone number---> "))
        if len(phone) != 11:
            print("Enter the right eleven digit number")
        else:
            phone_bill = int(input("Enter the amount to pay---> $"))
            if phone_bill > 150000:
                print("The amount is too high, please enter a lesser amount")
            else:
                print("The payment is successful")
    
    else:
        print("Invalid choice, please choose a valid option")

def mini_statement():
    print("...Mini Statement...")
    print("Choose the account type \n 1. Savings \n 2. Current")
    account_type = input(" ---> ")
    if account_type == "1":
        print("You have chosen to view your savings account mini statement")
        savings = int(input("Enter your account number---> "))
        if savings.isdigit():
            print("Your mini savings statement is as follows:")
            print("Date | Debit | Credit | Balance")
            print("------------------------------------------------")
            print("2022-01-01 | 1000 | 500 | 15000")
            print("2022-01-02 | 2000 | 1000 | 160")
            print("2022-01-03 | 3000 | 2000 | 170")
        else:
            print("Enter a valid savings account number")
    
    elif account_type == "2":
        print("You have chosen to view your current account mini statement")
        current = int(input("Enter your account number---> "))
        if current.isdigit():
            print("Your mini current statement is as follows:")
            print("Date | Debit | Credit | Balance")
            print("------------------------------------------------")
            print("2022-01-01 | 1000 | 500 | 15000")
            print("2022-01-02 | 2000 | 1000 | 160")
            print("2022-01-03 | 3000 | 2000 | 170")
        else:
            print("Enter a valid current account number")

    else:
        print("Invalid choice, please choose a valid option")

def other_options():
    print("...Other Options...")
    print("Choose the option \n 1. Check Balance \n 2. Deposit Money \n 3. Change Pin \n 4. Block Card \n 5. Request New Card \n 6. Purchase Prepaid Card \n 7. main menu")
    option = input(" ---> ")

    if option == "1":
        print("You have chosen to check your balance")
        print("Your current balance is $1000")

    elif option == "2":
        print("You have chosen to deposit money")
        deposit = int(input("Enter the amount you want to deposit ---> "))
        if deposit > 0:
            print("Insert cash into ATm deposit slot")
            print(" ")
            print("...Deposit successful...")

    elif option == "3":
        print("You have chosen to change your pin")
        current_pin = int(input("Enter your current pin---> "))
        if current_pin == user_pin:
            new_pin = int(input("Enter your new pin---> "))
            confirm_pin = int(input("Confirm your new pin---> "))
            if new_pin == confirm_pin:
                print("Pin changed successfully")
            else:
                print("Pin change failed, please try again")
        else: 
            print("Incorrect pin, please try again")
    
    elif option == "4":
        print("You have chosen to block your card")
        block_card= input("Are you sure you want to block your card (yes/no)---> ").lower()
        if block_card == "yes":
            print("Card blocked successfully")
        elif block_card == "no":
            print("Card blocking cancelled")

    elif option == "5":
        print("You have chosen to request a new card")
        print(" ")
        print("Request Successfully Accepted")
        print(" ")
        print("Card will be delivered to your address within 7-10 working days")
    
    elif option == "6":
        print("You have chosen to purchase a prepaid card")
        print(" ")
        print("Prepaid card purchased successfully")
        print(" ")
        print("Card details will be sent to your email address")
    
    elif option == "7":
        return welcome()
    
    else:
        print("Invalid option, please choose a valid option")



print("...You are welcome to Pelumi's ATM machine")
print(" ")
user_pin = input("Kindly input your pin---> ")

if user_pin is None:
    print("Error: PIN is required to access transactions.")
else:
    if len(user_pin) != 4:
        print("Error: PIN must be 4 digits.")
    elif not user_pin.isdigit():
        print("Error: PIN must be a numeric value.")
    else:
        # PIN is valid, allow access to transactions
        print("PIN is valid. Access granted.")

welcome()
#else:
 #   print("Welcome to Pelumi's ATM machine")



user_option = input("Please select your choice---> ")
if user_option == "1":
    print("You have chosen to withdraw cash")
    print("_____________________________________")
    cash_withdrawal()
elif user_option == "2":
    print("You have chosen to check your balance")
    print("_____________________________________")
    balance_inquiry()
elif user_option == "3":
    print("You have chosen to transfer funds")
    print("__________________________________")
    fund_transfer()
elif user_option == "4":
    print("You have chosen bills payment")
    print("______________________________")
    bills_payemnt()
elif user_option == "5":
    print("You have chosen mini statement")
    print("_______________________________")
    mini_statement()
elif user_option == "6":
    print("You have chosen other options")
    print("______________________________")
    other_options()
else:
    print("Invalid option, please choose a valid option")





