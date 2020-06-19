### Abstract Class

import abc

class Room(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def openDoor(self):
        pass
    @abc.abstractmethod
    def openWindow(self):
        pass

class BedRoom(Room):
    def openDoor(self):
        print('Open bedroom door')
    def openWindow(self):
        print('Open bedroom window')

class Lobby(Room):
    def OpenDoor(self):
        print('Open lobby door')

room1 = BedRoom()
print(issubclass(BedRoom, Room), isinstance(room1, Room))

lobby1 = Lobby()
print(issubclass(Lobby, Room), isinstance(lobby1, Room))


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