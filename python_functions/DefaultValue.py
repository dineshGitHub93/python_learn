def student(first_name, last_name = "Mark", standard ="Fifth"):

    print(first_name, last_name, 'studies in', standard, 'standard')

student("Samuel")

student("John", "cena", "Eighth")

# 1 keyword arguments
student(first_name="David")

# 2 keyword arguments
student("Mark", last_name="zooberg", standard="twelth")

# 2 keyword arguments 
student(standard="Seventh", first_name="samantha", last_name="Ruth")


def biograph(name, age):
    print(f"His name is {name}, and age is {age}".format(name, age))

biograph("My_love", 1)
biograph(1, "my_live")