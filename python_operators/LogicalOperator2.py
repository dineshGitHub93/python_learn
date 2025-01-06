# Logical operators = Allow us to Evaluate multiple conditions like (or, and & Not)
#                      or = at least one condition must be TRUE
#                      and = both condition must be TRUE    
#                      not = inverts the condition (Not False, Not True)

temp = -5
is_SUNNY = True

if temp >=28 and is_SUNNY:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp < 0 and is_SUNNY:
    print("It is COLD outside")
    print("It is SUNNY")
elif temp > 0 and temp <=27 and is_SUNNY:
    print("It is WARM outside")
    print("It is SUNNY")