#Python while loop with break statement

while True:

    user_input = input("Enter your name :")

    #Terminate the loop when user enters "end"
    if user_input == 'end':
        print("Loop has been ended")
        break

#Name prints here    
print(f"Name enetered {user_input}")