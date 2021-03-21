import random,string,os

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

# Password generator
finalPass = x + y + n + z
print("Welcome to Jokrr's password generator")
print("Generating Password...")
print(finalPass)
print("Please make a note of this password")
os.system("pause")