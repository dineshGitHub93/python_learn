# Logical operators = Allow us to Evaluate multiple conditions like (or, and & Not)
#                      or = at least one condition must be TRUE
#                      and = both condition must be TRUE    
#                      not = inverts the condition (Not False, Not True)

temp = 20
is_raining = False

if temp >= 38 or temp < 0 or is_raining:
    print("The outdoor event is cancelled ")
else:
    print("The outdoor event is still scheduled ") 