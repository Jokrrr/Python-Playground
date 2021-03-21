class Staff:
    def __init__ (self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print("Creating Staff Object")

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d"%(self._position, self.name, self.pay)
    @property
    def position(self):
        print("Getter Method")
        return self._position

    @position.setter
    def position(self, value):
        if value == "Manager" or value == "Basic":
            self._position = value
        else:
            print("Position is invalid. No Changes Made.")
    
    def calculatePay(self):
        prompt = "\nEnter number of hours worked for %s: "%(self.name)
        hours = input(prompt)
        prompt = "Enter the hourlay rate for %s:"%(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay
