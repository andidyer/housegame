class Item:
    def __init__(self,name,description):
        self.name=name.split(' ')
        self.description=description

    def getInfo(self):
        print(self.name+':\n'+self.description)

class MoveableItem(Item):
    def take(self):
        #Adds it to player inventory, pops it from room/box contents.
        pass

    def drop(self):
        #Pops from player inventory, adds to room inventory.
        pass

    def place(self,box):
        #Pops from player inventory, adds to box inventory

class ImmoveableItem(Item):
        pass

class Key(MoveableItem):
    def __init__(self,name,description,unlocks):
        super().__init__(name,description)
        self.unlocks=unlocks

    def unlock(self,Door):
        if Door in self.unlocks:
            Door._unlock()
        else:
            print('This key does not unlock this door')

class Flashlight(MoveableItem):
    def __init__(self,name,description):
        super().__init__(name,description)
        self.on=False

    def Switch(self):
        if self.on==False:
            print('You switch on the flashlight.')
            self.on=True
        elif self.on==True:
            print('You switch off the flashlight.')
            self.on=False

    def getInfo(self):
        if self.on:
            state='The flashlight is currently on.'
        elif not self.on:
            state='The flashlight is currently off.'
        print('{}\n{}\n{}'.format(self.name,self.description,state))

class Battery(MoveableItem):
    def __init__(self,name,description,remaining):
        super().__init__(name,description)
        self.remaining=remaining

class Door(ImmoveableItem):
    def __init__(self,name,description,room1,room2,locked=False,closed=True):
        super().__init__(name,description)
        self.room1=room1
        self.room2=room2
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

    def bang(self):
        if self.closed:
            print('You bang on the door.')
            print('Help!  Help!  Let me out of here!')
            print()
            time.sleep(5)
            print('No one can hear you.')
        elif not self.closed:
            print('It\'s strange behaviour to bang on an open door, no?')

class Terminal(ImmoveableItem):
    def __init__(self,name,description,password):
        super().__init__(name,description)
        self.password=password

class Room:
    def __init__(self,name,description,items,dark=False,*Portals):
        self.name=name
        self.description=description
        self.items
        self.dark=dark
        self.Portals=Portals

    def lookAround(self):
        if self.dark and not(flashlight in player.inventory and flashlight.on):
            print('It\'s pitch dark in here.  You can\'t see anything.')
        else:
            print('You are in {}.\n{}'.format(self.description))

class Portal:
    def __init__(self,orientation,Room1,Room2,Door):
        self.orientation=orientation
        self.Room1=Room1
        self.Room2=Room2
        self.door=door
        

class Player:
    def __init__(self):
        self.inventory=[]
        self.location='Hall'

    def move(self,direction):
        #Needs getPortal function from room; check if that portal's door is blocking the way.
        #If not, move the player to the other room beyond the portal.
        pass

    def getInventory(self):
        return tuple(self.inventory)

    def getLocation(self):
        return self.location.lookAround()
