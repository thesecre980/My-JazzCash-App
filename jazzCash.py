
# JazzCash App
def show_balance(balance):
    print(f"***** Your Balance is Rs.{balance} *****")

def send_money(balance):
    try:
        send_amount = int(input("Enter the amount to send: "))
        # Check if the amount is valid
        if send_amount <= 0:
            print("***** Please enter a valid amount *****")
            return balance
        # Check if the user has enough balance to send the amount
        elif send_amount > balance:
            print("***** You have insufficient balance *****")
            return balance
        # If the amount is valid and the user has enough balance
        else:
            print(f"****** Your {send_amount} amount sent successfully *******")
            return balance - send_amount
    except ValueError:
        # if the user enters a string or any other invalid input
        print("***** Please enter a valid number *****")
        return balance

def jazz_load(balance, load_num):
    try:
        # Get the amount to load
        load = int(input("Enter Jazz Load Amount: "))
        # Check if the amount is valid
        if load <= 0:
            print("***** Please enter a valid amount *****")
            return balance
        # Check if the user has enough balance to load the amount
        elif load > balance:
            print("***** You have insufficient balance *****")
            return balance
        l_no = int(input("Enter your load number: "))
        # Check if the load number is valid
        if l_no == load_num:
            print(f"***** Your {load} load to number {l_no} is successfully loaded *****")
            return balance - load
        # If the load number is invalid
        else:
            print("***** Please enter a valid number *****")
            return balance
        # If the amount is valid and the user has invalid number
    except ValueError:
        print("***** Please enter a valid number *****")
        return balance

balance = 500
load_num = 9230123
is_running = True

while is_running:
    print("Welcome to my JazzCash App")
    print("1. Check Balance")
    print("2. Send Money")
    print("3. Jazz Load")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        # if the user choice is 1 then show the balance
        show_balance(balance)
    elif choice == "2":
        # if the user choice is 2 then send the money
        balance = send_money(balance)
    elif choice == "3":
        # if the user choice is 3 then load the jazz
        balance = jazz_load(balance, load_num)
    elif choice == "4":
        # if the user choice is 4 then exit the app
        is_running = False
        # if the user enters any other choice
    else:
        print("**** Please enter a valid choice *****")

print("***** Thanks for using my JazzCash App. Have a good day *****")
