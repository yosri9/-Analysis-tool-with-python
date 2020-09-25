

class Exchange():
    def __init__(self, id=None, exchangeName=None, ipAddress=None, userName=None, password=None):
        self.id = id
        self.exchangeName = exchangeName
        self.ipAddress = ipAddress
        self.userName = userName
        self.password = password

    def table(self):
        return 'exchanges'

    def toMap(self):
        return (
            self.id ,
            self.exchangeName,
            self.ipAddress,
            self.userName,
            self.password
        )


    def exchangeFromMap(self, map):
        self.id = map[0]
        self.exchangeName = map[1]
        self.ipAddress = map[2]
        self.userName = map[3]
        self.password = map[4]
    @classmethod
    def table(self):
        return 'exchanges'

    def getID(self):
        return self.id
