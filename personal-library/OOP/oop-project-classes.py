import sys

#system Funcs
def closeprogram():
    print("Closing Program...")
    sys.exit()

class Staff():
    companyName = "OP Systems LTD"

    def __init__(self, fname, lname, position, salary):
        self.__fname = fname
        self.__Lname = lname
        self.__salary = salary
        self.__position = position
    def __str__(self):
        return "Position = %s, Name = %s , Salary = %d"%(self.__position, self.__fname + self.__Lname, self.__salary)
    #getter methods
    def get_fname(self):
        print("Getting Value")
        return self.__fname
    def get_Lname(self):
        print("Getting Value")
        return self.__Lname
    def get_salary(self):
        print("Getting Value")
        return self.__salary
    def get_position(self):
        print("Getting Value")
        return self.__position
    
    #setter methods
    def set_fname(self,x):
        print("Setting Value")
        self.__fname = x
    def set_Lname(self,y):
        print("Setting Value")
        self.__Lname = y
    def set_salary(self,z):
        print("Setting Value")
        self.__salary = z
    def set_position(self,value):
        print("Setting Value")
        if value == "CEO":
            print("Position is invalid. No changes made.")
        else:
            self.__position = value

    salary = property(get_salary, set_salary)
    name = property(get_fname, set_fname)
    Lname = property(get_Lname, set_Lname)
    position = property(get_position, set_position)

    def userNameGen(self):
        userNameGen = Staff.get_Lname + Staff.get_fname
        print(userNameGen)
    
    def newStaff(self, newStaffFName, newStaffLName, newStaffPosition, newStaffSalary):
        newStaffFName = input("Please enter the new staff members first name: ")
        newStaffLName = input("Please enter the new staff members last name: ")
        newStaffPosition = input("Please enter the new staff members position: ")
        newStaffSalary = input("Please enter the new staff members salary : ")
        newStaffFile = Staff(newStaffFName, newStaffLName, newStaffPosition, int(newStaffSalary))
        print("Displaying New Staff Record")
        print(newStaffFile)
        accountCheck = input("Would you like a username to be generated? ").upper()
        if accountCheck == "Y":
            Staff.userNameGen(self)
        else:
            closeprogram()

staffClass1 = Staff("Charlie","Noble","Manager",25000)
staffClass1.newStaff()