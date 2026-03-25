from main import *
def askToRestart():
    print("Would you like to calculate more or exit?")
    print("1. Go back to the start menu")
    print("2. Exit")
    askToRestartSelection = str(input("Select : "))
    print(" ")
    askToRestartSelected = int(askToRestartSelection)
    if askToRestartSelected == 1:
        mainMenu()
    elif askToRestartSelected == 2:
        print("Exiting!")
    #end
#end