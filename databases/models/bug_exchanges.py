

class BugExchange():
    def __init__(self,  bugID = None, exchangeID=None):
        self.bugID = bugID
        self.exchangeID = exchangeID

    def table(self):
        return 'bug_exchanges'

    def toList(self):
        return (
            self.bugID ,
            self.exchangeID,
        )


    def bug_exchangeFromList(self, list):
        self.bugID = list[0]
        self.exchangeID = list[1]

    @classmethod
    def table(self):
        return 'bug_exchanges'

    def getBugID(self):
        return self.bugID

    def getExchangeID(self):
        return self.exchangeID
