import random,string,os

print("Welcome to Jokrr's Onboarding Application")

#Username Generation

firstName = input("Please enter the new starters first name\n")
lastName = input("Please enter the new starts last name\n")

userName = firstName + "." + lastName

userNameUpper = userName.upper()

userNameDigit =  str(random.randint(0,100))
finalUserName = userNameUpper + userNameDigit

# Department

userDepartment = input("Please enter the new starters department\n")

userDepartmentFinal = str(userDepartment.upper())

# Password Generator

# Password Letters
lowerCaseLetters = string.ascii_lowercase
lowerCaseList = list(lowerCaseLetters)
upperCaseLetters = string.ascii_uppercase
upperCaseList = list(upperCaseLetters)
lowerCaseRand = random.choices(lowerCaseList, k=2)
upperCaseRand = random.choices(upperCaseList, k=2)
x = "".join(lowerCaseRand)
y = "".join(upperCaseRand)

# Password Numbers
firstNumberRand = random.randint(0,100)
secondNumberRand = random.randint(0,100)

n = str(firstNumberRand + secondNumberRand)


# Password Special Characters
specialCharactersList = ["!","£","$","%","&","*"]
specialCharacterRand = random.choices(specialCharactersList, k=6)
z = "".join(specialCharacterRand)

# Actual generation
finalPass = x + y + n + z # Fairly secure and long

# Final Output

print("Here are the new starters details!")
print("Username: ", finalUserName)
print("Password: ", finalPass)
print("Department: ", userDepartmentFinal)
print("Please make a note of these details")
os.system("pause")
