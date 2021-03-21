import time, datetime, sys, jokrr_config

def login():
    print('Enter correct username and password combo to continue')
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password == jokrr_config.passid and username == jokrr_config.userid:
        print('Access granted')
        time.sleep(1)
    else:
        accessdenied()

def accessdenied():
    print('Access denied. Try again.')
    time.sleep(.5)
    print("Reloading...")
    time.sleep(.5)
    login()