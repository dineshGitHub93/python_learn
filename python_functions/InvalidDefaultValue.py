#Create a default function

def student(first_name, last_name="Kumar", standard="secound"):
    print(first_name, last_name, 'studies in', standard, 'standard')

#Required argument missing 
student()

#Non keyword arguments after a keyword arguments 
student(first_name='Raj', "fourth")

#unknown keyword argument
student(subject='science')