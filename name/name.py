import sys, functions, datetime
print("Hello! My name is Python! ")
UserName = input("What is your name?\n")
if UserName == "Chanelle" or UserName == "chanelle":
    functions.chanelle()
if UserName == "Lisa" or UserName == "lisa":
    functions.lisa()
print("Its nice to meet you " + UserName + "!")

if UserName == "andy" or UserName == "Andy":
    functions.andy()

NameLength = len(UserName)
print("Your name is " + str(NameLength) + " letters long.")
def errorMsg():
    print("Error: Please enter numbers only!")
    userAgeFunc()


def userAgeFunc():
    userAge = input("What year was you born?\n")
    now = datetime.datetime.now()
    if userAge.isdigit():
        yob = now.year - int(userAge)
        print("You are " + str(int(yob)) + " years old.")
        print("In one year you will be " + str(int(yob) + 1) + " years old.")
        print("You was born in the year", str(int(userAge)) + ".")  
    else:
        errorMsg()
        
userAgeFunc()

closeprogram = sys.exit
closecheck = input("Press enter to close the program")

if closecheck == True:
    closeprogram

