"""
dividerone = int(input("what should the first divider be?: "))
dividertwo = int(input("what should the second divider be?: "))
for i in range(1,101):
    if i%(dividerone) ==0 and i%(dividertwo) ==0:
        print("fizzbuzz")
    elif i%(dividerone) ==0:
        print("fizz")
    elif i%(dividertwo) ==0:
    else:
       print(i)
"""


def fizzbuzz(inputnumber):
    if inputnumber % 3 == 0 and inputnumber % 5 == 0:
        return "fizzbuzz"
    elif inputnumber % 3 == 0:
        return "fizz"
    elif inputnumber % 5 == 0:
        return "buzz"
    else:
        return inputnumber
