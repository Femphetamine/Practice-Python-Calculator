def startMenu():
    print("What do you want to calculate?")
    print("Input a number as your option")
    print("1. Basic calculation (2 Inputs max)") # extremely basic, revising soon
    print("2. Fahrenheit to celsius (and vice versa)")
    print("3. Metrics to imperial(US) (and vice versa)")
    # TODO: Percentages
    # TODO: Circles?
    starterInput = str(input("Select : ")) # ig to make the else statement below work?
    selection = int(starterInput)
    if selection == 1:
        print(" ")
        basicCalculations()
    elif selection == 2:
        print(" ")
        fahrenheitToCelsius()
    elif selection == 3:
       print(" ")
       metricConversion() 
    else:
        print("Something went wrong")
        askToRestart()
    #end
#end

def askToRestart():
    print("Would you like to calculate more or exit?")
    print("1. Go back to the start menu")
    print("2. Exit")
    askToRestartSelection = str(input("Select : "))
    print(" ")
    askToRestartSelected = int(askToRestartSelection)
    if askToRestartSelected == 1:
        startMenu()
    elif askToRestartSelected == 2:
        print("Exiting!")
    #end
#end
startMenu()