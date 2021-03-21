import random,string,os

passInp = input("Please enter your last name\n")

firstNumberRand = random.randint(0,100)
secondNumberRand = random.randint(0,100)

n = str(firstNumberRand + secondNumberRand)

passgen = passInp + n

print(passgen)
os.system("pause")