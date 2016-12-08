from .person import Person
#from docopt import docopt
#print (docopt(__doc__))
class Amity(object):
    ''' amity class creates multiple rooms and allocates to persons'''

    def __init__(self):

        self.offices=[]
        self.lspace=[]
        self.rooms=self.offices +self.lspace
        self.fellows=[]
        self.staff=[]
        self.person=self.staff+self.fellows
        self.rm_occupancy={}
        self.pending=[]

    def create_room(self,rm_name,rm_type):
        '''create a room instance and append it to the rooms lists.'''

        if rm_name in self.rooms:
            raise ValueError("A room with same name already exist")
        if rm_type=='Office':
            rm_name=Office(rm_name)
            self.offices.append(rm_name)

        elif rm_type=='LivingSpace':
            rm_name=LivingSpace(rm_name)
            self.lspace.append(rm_name)

        self.rooms=self.offices +self.lspace
        self.rm_occupancy={rm_name.rm_name:[]}


    def allocate_room(self):
        



    def view_all_rooms(self):
        print ('List of all rooms',self.rm_occupancy)

    def print_room(self):
        print ('List of all occupants in room',self.rm_occupancy[rm_name])

    def print_unallocated(self):
        print ('List of all unallocated persons',self.pending)

    def load_people(self):
        pass


class Room (object):
    ''' Room class creates the object attributes of the room'''
    def __init__(self,rm_name):
        self.rm_name = rm_name
        self.occupants=[]
        if type(self.rm_name)!=str:
            raise TypeError("Room name can only be a string")

    @property
    def room_type(self):
        return self.__class__.__name__


class Office(Room):
    #rm_size=6
    def __init__(self,rm_name):
        super(Office, self).__init__(rm_name)
        self.rm_name=rm_name
        self.rm_size=6


class LivingSpace(Room):
    #rm_size=4
    def __init__(self,rm_name):
        super(Office, self).__init__(rm_name)
        self.rm_name=rm_name
        self.rm_size=6