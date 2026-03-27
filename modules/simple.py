import os

def basicCalculating():
    # i have to learn dynamic variables at some point
    os.system('cls' if os.name == 'nt' else 'clear')
    n1 = float(input("First digit(s) : "))
    print(" ")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print(" ")
    op = int(input("Select : "))
    n2 = float(input("Second digit(s) : "))
    if op == 1:
        t = n1 + n2
        print(f"{n1} + {n2} = {t}")
        print(f"= {t}")
    elif op == 2:
        t = n1 - n2
        print(f"{n1} - {n2} = {t}")
        print(f"= {t}")
    elif op == 3:
        t = n1 * n2
        print(f"{n1} * {n2} = {t}")
        print(f"= {t}")
    elif op == 4:
        t = n1 / n2
        print(f"{n1} / {n2} = {t}")
        print(f"= {t}")
    #end
#end