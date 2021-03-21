import time, datetime, sys
import securitycheck, jokrr_config, game

# Functions
def returntomenu():
    time.sleep(.5)
    returntomenu = input("Would you like to return to the menu?(y/n)")
    if returntomenu == "y" or returntomenu == "Y":
        print("Returning to Menu...")
        mainmenu()
    elif returntomenu == "n" or returntomenu == "N":
        closecheck()
    elif returntomenu != "y" or returntomenu != "Y" or returntomenu != "n" or returntomenu != "N":
        print("Input not recognised")
        print("Reloading Script...")


def closecheck():
    closecheck = input("This will close the program do you want to continue?(y/n)")
    if closecheck == "y" or closecheck == "Y":
            closeprogram()
    elif closecheck == "n" or closecheck == "N":
            print("Returning to Main Menu")
            time.sleep(.5)
            mainmenu()


def option1():
    print("-----FAQ-----")
    time.sleep(.5)
    print("Here are some frequently asked questions:")
    time.sleep(.5)
    now = datetime.datetime.now()
    age = now.year - int(2002)
    print("1: How old are you? I am " + str(age))
    print("2: Where are you from? I am from Essex in the UK")
    print("3: What is your favourite colour? My favourite colour is purple ")
    returntomenu()
    option1()
    closecheck()


def option2():
    print("-----Game-----")
    print("Here you can play Rock,Paper,Scissors!:")
    game.rps()
    returntomenu()
    option2()
    closecheck()

def option3():
    print("-----Write To File-----")
    print("Here you can write an input to a file: ")
    data = input("Please input:")
    f = open("Info_Output.txt","w")
    f.write(" " +data)
    f.close()
    print("Printing Input")
    time.sleep(.5)
    r = open("Info_Output.txt","r")
    print(r.read())
    r.close()
    returntomenu()
    option3()
    closecheck()

def closeprogram():
    print("Closing Program...")
    time.sleep(.5)
    sys.exit()
# Performs login check
securitycheck.login()
# Main Menu
def mainmenu():
    print("Welcome to Jokrr's Program!")
    time.sleep(.5)
    print("Main Menu")
    print("Please Select an option:")
    time.sleep(.5)
    print("Option 1:FAQ")
    time.sleep(.5)
    print("Option 2:Game")
    time.sleep(.5)
    print("Option 3:Write to File")
    time.sleep(.5)
    print("Option 4: Exit Program")
# Input
    selection = input("Please select a Number:")
    print("You Have selected: Option " + selection)
# Input check
    if selection == "1":
        print("Loading...")
        time.sleep(.5)
        option1()
    elif selection == "2":
        print("Loading...")
        time.sleep(.5)
        option2()
    elif selection == "3":
        print("Loading...")
        time.sleep(.5)
        option3()
    elif selection == "4":
        closecheck()
    else:
        print("Input not recognised")
        print("Reloading...")
        time.sleep(.5)
        mainmenu()
mainmenu()