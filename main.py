# Run this program to run the calculator!!!



from modules.simple import basicCalculating
import os


# < --- Main menu --- >
def startMenu():
    print("-- Main menu --")
    print("Select an option by entering a number!")
    print("1. Basic calculating")
    select = int(input("Select : "))
    if select == 1:
        basicCalculating()
    elif select == 2:
        None #temperatureConverting
    else:
        print("Err")
    #end
#end

startMenu()

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

restartMenu()