import random,string

lowerCaseLetters = string.ascii_lowercase
lowerCaseList = list(lowerCaseLetters)
upperCaseLetters = string.ascii_uppercase
upperCaseList = list(upperCaseLetters)
lowerCaseRand = random.choices(lowerCaseList, k=2)
upperCaseRand = random.choices(upperCaseList, k=2)

x = "".join(lowerCaseRand)
y = "".join(upperCaseRand)
print(x+y)