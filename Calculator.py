# personally like to add end, to the end of each def.
# just makes it easier to read for me coming from Lua
def basicCalculations(): # First version of the calculator
    input1 = float(input("First input : "))
    input2 = float(input("Second input : "))
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
# end
def fahrenheitToCelsius():
    print("Converting fahrenheit to celsius")
    input1 = float(input("Degrees (F) : "))
    x = input1 - 32
    y = 5 / 9
    z = x * y
    print(f"{input1} Degrees (F) is {z} Celsius")
    if z < 0:
        print(f"{z} Celsius = Freezing")
    elif z < 10:
        print(f"{z} Celsius = Cool")
    elif z < 20:
        print(f"{z} Celsius = Room temp")
    elif z < 30:
        print(f"{z} Celsius = Warm")
    elif z < 37.8:
        print(f"{z} Celsius = Hot")
    elif z < 100:
        print(f"{z} Celsius = Boiling")
# end

# <--           --          -->
print("What do you want to calculate?")
print("Input a number as your option")
print("1. Basic calculation (2 Inputs max)") # extremely basic, revising soon
print("2. Convert fahrenheit to celsius")
print("3. Percentages") # döh
starterInput = str(input("Select : "))
selection = int(starterInput)
if selection == 1:
    basicCalculations()
if selection == 2:
    fahrenheitToCelsius()
else:
    print("Something went wrong")