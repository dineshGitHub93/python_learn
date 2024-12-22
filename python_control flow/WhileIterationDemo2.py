
#The while loop is usually used when the number of iterations is unknown.

while True:
    user_input = input("Enter password here :")

    if user_input == 'exit':
        print(f"Password Rejected ")
        break

    print(f"Statu : Enter Allowed ")