### Polymorphism 1

class Building:
    strAddress = "Daejeon"
    def opendoor(self):
        print('Door Opened!')

class Hotel:
    def openDoor(self):
        print('Bellboy opens a door')
    def checkIn(self):
        print('Someone checks in for 1 day')
    def checkIn(self, days):
        print('Someone checks in for', days, 'days')

motel = Building()
motel.strAddress
motel.opendoor()

lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkIn()
lotteHotel.checkIn(3)
