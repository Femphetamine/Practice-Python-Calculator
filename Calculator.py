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
    #end
#end
def fahrenheitToCelsius():
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    selectConversion = str(input("Select : "))
    conversionSelected = int(selectConversion)

    if conversionSelected == 1:
        print("Converting fahrenheit to celsius")
        FtoC = float(input("Degrees (F) : "))
        calculation = (FtoC - 32) * (5 / 9)
        print(f"{FtoC} Degrees (F) is {calculation} Celsius")
        if calculation < 0:
            print(f"{calculation} Celsius = Freezing")
        elif calculation < 10:
            print(f"{calculation} Celsius = Cool")
        elif calculation < 20:
            print(f"{calculation} Celsius = Room temp")
        elif calculation < 30:
            print(f"{calculation} Celsius = Warm")
        elif calculation < 37.8:
            print(f"{calculation} Celsius = Hot")
        elif calculation < 100:
           print(f"{calculation} Celsius = Boiling")
    elif conversionSelected == 2:
        CtoF = float(input("Degrees (C) : "))
        calculation = CtoF * (9 / 5) + 32
        print(f"{CtoF} Degrees (C) is {calculation} Fahrenheit")
    else:
        print("Something went wrong, did you select using an integer?")
    #end
#end

# <--           --          -->
print("What do you want to calculate?")
print("Input a number as your option")
print("1. Basic calculation (2 Inputs max)") # extremely basic, revising soon
print("2. Fahrenheit to celsius (and vice versa)")
print("3. Percentages") # döh
starterInput = str(input("Select : ")) # ig to make the else statement below work?
selection = int(starterInput)

if selection == 1:
    basicCalculations()
elif selection == 2:
    fahrenheitToCelsius()
else:
    print("Something went wrong")
#end