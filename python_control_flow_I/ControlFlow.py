age = int(input("Enter your age here! "))

"""if age>=18:
    print("Eligible to vote")
else:
    print("Not elibible to vote")
"""
if age >=0 and age <=5:
    print("Baby is not eligible to join the school")
elif age >=6 and age<=10:
    print("Child should have completed primary education")
elif age >=11 and age<=15:
    print("Child should have completed high school education")
elif age >=16 and age<=17:
    print("Child should have completed higher secoundary education")
elif age >=18 and age<=21:
    print("Child should have completed 3 or 4 years graduate")
else:
    print("Should join the company and persuing the career")