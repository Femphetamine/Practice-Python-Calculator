# Run this program to run the calculator!


from modules.temp import tempCalc
from modules.simple import basicCalculating
import os
# < --- Restart menu --- >
# <summary>
# function is called when another function ends
# </summary>
def restartMenu():
    print(" ")
    print("Program finished")
    print("1. Back to the main menu (Continue using)")
    print("2. Exit")
    select = int(input("Select : "))
    if select == 1:
        print(" ")
        os.system('cls' if os.name == 'nt' else 'clear')
        startMenu()
    elif select == 2:
        print("Bye bye!")
    #end
#end

# < --- Main menu --- >
def startMenu():
    print("-- Main menu --")
    print("Select an option by entering a number!")
    print("1. Basic calculating")
    print("2. Temperature conversion")
    select = int(input("Select : "))
    if select == 1:
        basicCalculating()
    elif select == 2:
        tempCalc()
    else:
        print("Err")
    #end
    restartMenu()
#end

startMenu()