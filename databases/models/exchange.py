

class Exchange():
    def __init__(self, id=None, exchangeName=None, ipAddress=None, userName=None, password=None):
        self.id = id
        self.exchangeName = exchangeName
        self.ipAddress = ipAddress
        self.userName = userName
        self.password = password



    def toList(self):
        return (
            self.id ,
            self.exchangeName,
            self.ipAddress,
            self.userName,
            self.password
        )



    @classmethod
    def table(self):
        return 'exchanges'

    def getID(self):
        return self.id
    def getName(self):
        return self.exchangeName
