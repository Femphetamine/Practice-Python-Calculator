def basicCalculations(): # First version of the calculator
    input1 = float(input("First input: "))
    input2 = float(input("Second input: "))
    print("1. Plus")
    print("2. Minus")
    print("3. Times")
    print("4. Divide")
    operator = input("Selection : ")
    operator = operator.lower()
    if operator == "plus" or operator == "1":
        total = input1 + input2
        print(f"{input1} + {input2}")
        print(f"Equals to: {total}")
    elif operator == "minus" or operator == "2":
        total = input1 - input2
        print(f"{input1} - {input2}")
        print(f"Equals to: {total}")
    elif operator == "times" or operator == "3":
        total = input1 * input2
        print(f"{input1} * {input2}")
        print(f"Equals to: {total}")
    elif operator == "divide" or operator == "4":
        total = input1 / input2
        print(f"{input1} / {input2}")
        print(f"Equals to: {total}")
    else:
        print("Error with inputting operator, did you write the operator properly?")

# <--           --          -->
print("What do you want to calculate?")
print("Input a number as your option")
print("1. Basic calculation (2 Inputs max)") # extremely basic, revising soon
print("2. Convert fahrenheit to celsius")
print("3. Percentages") # döh
starterInput = input("Selection : ")
selection = int(starterInput)
if selection == 1:
    basicCalculations()
else:
    print("Something went wrong")