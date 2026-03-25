from main import startMenu

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