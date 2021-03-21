try:
    print(x)
except NameError:
    print("Error: Variable Not Defined")
except Exception as e:
    print("Unknown Error: ", e)