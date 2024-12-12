#Beginner banking projects

#function for displaying balance
def show_balance():
    print(f"Your current balanace is :{balance: .2f}")

#function for depositing the money
def deposit():
    amount = float(input("please enter your deposite amount: "))
    
    if amount <=0:
        print("That's not a valid amount ")
        return 0
    else :
        return amount    

#function for withdrawing the money
def withdraw():

    amount = float(input("Please enter the withdrawal amount "))

    if amount > balance:
        print(" Insufficient Fund...!")
        return 0
    elif amount == 0:
        print("Please enter valid amount...!")
    else:
         print(f"{amount: .1f} is withdrawn successfully...!")
         return amount
        

balance = 0
is_running = True
decorate = "*****************************"

while is_running :
    print(decorate)
    print("Banking program")
    print(decorate)
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choise (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
         balance -= withdraw()
        
    elif choice == '4':
        is_running = False
    else:
        print("Choise you're entred is not valid")
print("Thank you Have a nice day!")