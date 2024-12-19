
def raindriops(numbers):

    sounds = ""
    if numbers % 3 == 0:
        sounds += "pling"
    if numbers % 5 == 0:
        sounds += "plang"
    if numbers % 7 == 0:
        sounds += "plong"
    return sounds or str(numbers)

print(raindriops(21))