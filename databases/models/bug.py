

class Bug():
    def __init__(self, id, repetition, level, description):
        self.id = id
        self.repetition = repetition
        self.level = level
        self.description = description

    def table():
        return 'bugs'

    def toMap(self):
        return (
             self.id,
             self.repetition,
             self.level,
             self.description
        )

    def bugFromMap(self , map):
        self.id = map[0],
        self.repetition = map[1],
        self.level = map[2],
        self.description = map[3]

    def table(self):
        return 'bugs'

    def getID(self):
        return self.id