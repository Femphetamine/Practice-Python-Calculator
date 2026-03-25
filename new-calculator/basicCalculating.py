def basicCalculation():
    n1 = float(input("First number : "))
    n2 = float(input("Second number : "))
    print(" ")
    print("Enter operator (string)")
    operator = input("")
    if operator == "+":
        t = n1 + n2
        print(f"{n1} + {n2} = {t}")

#end