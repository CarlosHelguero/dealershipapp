class Customer:
    def __init__(self, firstName=None, lastName=None, email=None, phone=None,vetdisable=False):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__phone = phone
        self.__vetdisable = vetdisable

    def setfirstname(self, firstname):
        self.__firstname = firstname
    def setlastname(self, lastname):
        self.__lastname = lastname
    def setemail(self, email):
        self.__email = email
    def setphone(self, phone):
        self.__phone = phone
    def setvetdisable(self, vetdisable):
        self.__vetdisable= vetdisable

    def getfirstname(self):
        return self.__firstname
    def getlastname(self):
        return self.__lastname
    def getemail(self):
        return self.__email
    def getphone(self):

        return self.__phone 
    def getvetdisable(self):

        return self.__vetdisable



    






