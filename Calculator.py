def basicCalculations(): # First version of the calculator
    input1 = float(input("First input: "))
    input2 = float(input("Second input: "))
    print("1. Plus")
    print("2. Minus")
    print("3. Times")
    print("4. Divide")
    operator = input(": ")
    operator = operator.lower()
    if operator == "plus":
        total = input1 + input2
        print(f"{input1} + {input2}")
        print(f"Equals to: {total}")
    elif operator == "minus":
        total = input1 - input2
        print(f"{input1} - {input2}")
        print(f"Equals to: {total}")
    elif operator == "times":
        total = input1 * input2
        print(f"{input1} * {input2}")
        print(f"Equals to: {total}")
    elif operator == "divide":
        total = input1 / input2
        print(f"{input1} / {input2}")
        print(f"Equals to: {total}")
    else:
        print("Error with inputting operator, did you write the operator properly?")

# <--           --          -->
print("What do you want to calculate?")
print("Input number as your option or write the selections names")