dividerone = int(input("what should the first divider be?: "))
dividertwo = int(input("what should the second divider be?: "))
for i in range(1,101):
    if i%(dividerone) ==0 and i%(dividertwo) ==0:
        print("fizzbuzz")
    elif i%(dividerone) ==0:
        print("fizz")
    elif i%(dividertwo) ==0:
        print("buzz")
    else:
        print(i)