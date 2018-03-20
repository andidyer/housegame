import time
from pynput import keyboard

class Room:
    def __init__(self,name,description,items):
        self.name=name
        self.description=description
        self.items=items
        self.N=None
        self.E=None
        self.S=None
        self.W=None

    def addDoor(self,direction,door):
        if direction=='N':
            self.N=door
        if direction=='E':
            self.E=door
        if direction=='S':
            self.S=door
        if direction=='W':
            self.W=door

    def getInfo(self):
        print(self.name)
        print(self.description)

class Item:
    def __init__(self,name,description):
        self.name=name.split(' ')
        self.description=description

    def getInfo(self):
        print(self.name+':\n'+self.description)

class Door(Item):
    def __init__(self,name,description,room1,room2,locked=False,closed=False):
        super().__init__(name,description)
        self.room1=room1 #Room object
        self.room2=room2 #Room object
        self.locked=locked
        self.closed=closed

    def unlock(self):
        if self.locked:
            print('Door unlocked')
            self.locked=False
        else:
            print('Door is already unlocked')

    def open(self):
        if self.locked:
            print('This door is locked.')
        elif not self.closed:
            print('Door is already open')
        elif self.closed:
            self.closed=False
            print('Opened door')

    def otherSide(self):
        if player.getLocation()==self.room1:
            player.changeLocation(self.room2)
        elif player.getLocation()==self.room2:
            player.changeLocation(self.room1)

    def bang(self):
        if self.closed:
            print('You bang on the door.')
            print('Help!  Help!  Let me out of here!')
            print()
            time.sleep(5)
            print('No one can hear you.')
        elif not self.closed:
            print('It\'s strange behaviour to bang on an open door, no?')

class Player:
    def __init__(self):
        self.inventory=[]
        self.location=kitchen

    def getInventory(self):
        return tuple(self.inventory)

    def getLocation(self):
        return self.location

    def changeLocation(self,newRoom):
        self.location=newRoom

kitchen=Room('Kitchen','A kitchen',[])
storage=Room('Storage','A storage room',[])
bedroom=Room('Bedroom','A bedroom',[])
diningroom=Room('Dining Room','A dining room',[])

DoorSK=Door('White door','A white door',storage,kitchen,locked=False,closed=False)
DoorSB=Door('Red door','A red door',storage,bedroom,locked=False,closed=False)
DoorBD=Door('Blue door','A blue door',diningroom,bedroom,locked=False,closed=False)
DoorDK=Door('Black door','A black door',diningroom,kitchen,locked=False,closed=False)

kitchen.addDoor('W',DoorSK)
kitchen.addDoor('S',DoorDK)
storage.addDoor('E',DoorSK)
storage.addDoor('S',DoorSB)
bedroom.addDoor('N',DoorSB)
bedroom.addDoor('E',DoorBD)
diningroom.addDoor('W',DoorBD)
diningroom.addDoor('N',DoorDK)

player=Player()
