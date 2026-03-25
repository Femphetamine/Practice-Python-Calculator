from askRestart import *
from basicCalculating import *

def mainMenu():
    print("-- Main Menu --")
    print("1. Basic math")
    print("67. Debug")
    print(" ")
    print("Make your selection by entering a number")
    select = int(input("Select : "))
    if select == 1:
        basicCalculation()
    elif select == 67:
        askToRestart()
    else:
        print("Error with selection, did you enter a number properly?")
#end

mainMenu()