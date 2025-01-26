# show balance function
def show_balance():
    print(f"*****Your Balance is Rs.{balance}*****")
# send mony function
def send_mony():
    send_amount = int(input("Enter Your Send amount: "))
    # agar send amount balance k equal ya is sy kam ho tab ya print ho ga
    if send_amount <= balance:
        print(f" ******Your {send_amount} amount Send Successful******* ")
        return send_amount
    # agr send amount 0 ya is sy kam yani mins me ho tab ya print hoga
    elif send_amount <= 0:
        print("*****Please Enter a valid amount*****")
        return 0
    # agr send amount balance sy zayada ho tab ya print hoga
    elif send_amount > balance:
        print("*****You have insufficient Balance***** ")
        return 0
        
    else:
        return 0
def jazz_load():
    load = int(input("Enter Jazz Load Amount: "))
    # agr load ki raqam 0 ya is kam yani mins ho tab ya print ho ga
    if load <= 0:
        print("*****Please Enter a valid amount*****")
        return 0
    # agr load ki raaqam balance sy zyzda hoe tab ya print ho ga
    elif load > balance:
        print("*****You have insufficient balance*****")
        return 0
    
    l_no = int(input("Enter Your load No: "))
    # agr load no is equl to load num than print this
    if l_no == load_num:
        print(f"*****Your {load} Load in this Num {l_no} is Successful loaded*****")
        return 0
    # if no is not equal to load num than print this 
    elif l_no != load_num:
        print("*****Please Enter a valid no*****")
        return 0
    # if load amount is greater than balance than print this
    elif load > balance:
        print("*****You have insufficient balance: *****")
        return 0
    else:
        return 
    


balance = 500
load_num = 923012345678
is_running = True

while is_running:
    print("Welcome to my JazzCash App")
    print("1.Check Balance")
    print("2.Send Mony")
    print("3.Jazz Load")
    print("4.Exit")

    choice = input("Enter Your Choice No (1-4): ")
    if choice == "1":
        # if user choice 1 than show balance
        show_balance()
    elif choice == "2":
        # if user choice 2 than than send mony
        balance -= send_mony()
    elif choice == "3": 
        # if uer choice 3 than user send load
        balance -= jazz_load()
    elif choice == "4":
        is_running = False
    else:
        print("****Please Enter a Valid Choice*****")
        

print("*****Thanks For using my JazzCash App. Have a good day*****")
