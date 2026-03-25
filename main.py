from restartMenu import askToRestart

def startMenu():
    print("1. Debug")
    selection = int(input("Select : "))
    if selection == 1:
        askToRestart()
    else:
        print("Error!")
        askToRestart()
    #end
#end

def askToRestart():
    print("Program complete.")
    print("1. Restart program")
    print("2. Exit program")
    selection = int(input("Select : "))
    if selection == 1:
        startMenu()
    elif selection == 2:
        print("Bye bye!")
    #end
#end