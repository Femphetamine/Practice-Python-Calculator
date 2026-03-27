import os

def tempCalc():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    select = int(input("Select : "))
    print(" ")
    if select == 1:
        c = float(input("C : "))
        f = c * (9 / 5) + 32
        print(f"{c} Celsius is {f} Fahrenheit")
    elif select == 2:
        f = float(input("F : "))
        c = (f - 32) * (5 / 9)
        print(f"{f} Fahrenheit is {c} Celsius")
    else:
        print("Err")
    #end
#end