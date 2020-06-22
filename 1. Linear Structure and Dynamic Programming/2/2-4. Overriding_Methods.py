### Overriding Methods in object

class Room:
    numWidth = 100
    numHeight = 100
    numDepth = 100

    def __init__(self, parWidth, parHeight, parDepth):
        self.numDepth = parDepth
        self.numWidth = parWidth
        self.numDepth = parDepth

    def getVolume(self):
        return self.numDepth*self.numWidth*self.numHeight

    def __eq__(self, other):
        if isinstance(other, Room):
            if self.getVolume() == other.getVolume():
                return True
        return False

room1 = Room(100, 20, 30)
room2 = Room(100, 10, 60)
print(room1 == room2)