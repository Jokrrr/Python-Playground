# Jokrr's Calculator v0.1
import sys

calVer = "Calculator V0.2"

print(calVer)

# System Functions and Variables
def closeprogram():
    print("Closing Program...")
    sys.exit()

def returnCheck():
    rcheck = input("Do you want to return to the selections? (Y/N)").upper()
    if rcheck == "Y":
        print("Loading Selections")
        choicesPrint()
        selectionFunc()
    elif rcheck == "N":
        closecheck()

def closecheck():
    try:
        closecheck = input("This will close the program do you want to continue?(Y/N)").upper()
        if closecheck == "Y":
            closeprogram()
        elif closecheck == "N":
            print("Returning to selections")
            choicesPrint()
            selectionFunc()
    except ValueError:
        print("Value Error: You did not input a number")
        print("Reloading")
        closecheck()
    except Exception as e:
        print("Unknown Error: ", e)
        print("Reloading")
        closecheck()
    
# Math Functions
def addition():
    try:                         # Math and error catching
        x = input("Please enter a number: ")
        y = input("Please enter another number: ")
        a = int(x) + int(y)
        print(a)
        returnCheck()
    except ValueError:
        print("Value Error: You did not input a number")
        print("Reloading")
        addition()
    except Exception as e:
        print("Unknown Error: ", e)
        print("Reloading")
        addition()

def subtraction():
    try:                        # Math and error catching
        x = input("Please enter a number: ")
        y = input("Please enter another number: ")
        a = int(x) - int(y)
        print(a)
        returnCheck()
    except ValueError:
        print("Value Error: You did not input a number")
        print("Reloading")
        subtraction()
    except Exception as e:
        print("Unknown Error: ", e)
        print("Reloading")
        subtraction()

def multiplication():
    try:                         # Math and error catching
        x = input("Please enter a number: ")
        y = input("Please enter another number: ")
        a = int(x) * int(y)
        print(a)
        returnCheck()
    except ValueError:
        print("Value Error: You did not input a number")
        print("Reloading")
        multiplication()
    except Exception as e:
        print("Unknown Error: ", e)
        print("Reloading")
        multiplication()
def division():
    try:                         # Math and error catching
        divCheck = input("Do you want to round the answer? (Y/N)").upper()
        if divCheck == "Y":
            x = input("Please enter a number: ")
            y = input("Please enter another number: ")
            a = int(x) // int(y)
            print(a)
            returnCheck()
        elif divCheck == "N":
            x = input("Please enter a number: ")
            y = input("Please enter another number: ")
            a = int(x) / int(y)
            print(a)
            returnCheck()
        else:
            print("Input not recognised")
            print("Reloading")
            division()
    except ValueError:
        print("Value Error: You did not input a number")
        print("Reloading")
        division()
    except Exception as e:
        print("Unknown Error: ", e)
        print("Reloading")
        division()

def rounding():
    try:
        rouCheck = input("Do you want to round to a specific decimal? (Y/N)").upper()
        if rouCheck == "Y":
            x = input("Please enter a number: ")
            dc = input("How many decimal places do you want?")
            y = round(float(x), int(dc))
            print(y)
            returnCheck()
        else:
            x = input("Please enter a number: ")
            y = round(float(x))
            print(y)
            returnCheck()

    except ValueError:
        print("Value Error: You did not input a number")
        print("Reloading")
        rounding()
    except Exception as e:
        print("Unknown Error: ", e)
        print("Reloading")
        rounding()

def errorMsg():
    print("Error: An error has occurred")
    print("Attempting Reload")



# Prints options
def choicesPrint():
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Rounding")
    print("6: Exit Calculator")
choicesPrint()
# Input
def selectionFunc():
    choiceInp = input("What do you want to do? ")
    if choiceInp == "1":
        addition()
    elif choiceInp == "2":
        subtraction()
    elif choiceInp == "3":
        multiplication()
    elif choiceInp == "4":
        division()
    elif choiceInp == "5":
        rounding()
    elif choiceInp == "6":
        closecheck()
    else:
        errorMsg()
        selectionFunc()

selectionFunc()