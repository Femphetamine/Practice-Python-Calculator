from restartMenu import askToRestart
def startMenu():
    print("1. Debug")
    selection = int(input("Select : "))
    if selection == 1:
        askToRestart()
    else:
        print("Error!")
        askToRestart
#end