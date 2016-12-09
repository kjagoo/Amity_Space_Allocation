from .person import Person, Fellow, Staff
import random
#from docopt import docopt
#print (docopt(__doc__))
class Amity(object):
    ''' amity class creates multiple rooms and allocates to persons'''

    def __init__(self):
        self.offices=[]
        self.lspace=[]
        self.rooms=self.offices +self.lspace
        self.fellows=[]
        self.staffs=[]
        self.persons=self.staffs+self.fellows
        self.rm_occupancy={'uganda':[],'tanzania':[]}
        self.pending=[]
        self.allocated_persons=[]

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
        self.rm_occupancy[rm_name.rm_name]=[]

    def add_person(self,f_name,s_name,role):

        if role=='Fellow':
            f_name=Fellow(f_name,s_name,role)
            self.fellows.append(f_name)
        elif role=='Staff':
            f_name=Staff(f_name,s_name,role)
            self.staffs.append(f_name)
        self.persons=self.staffs+self.fellows

    def allocate_room(self,f_name,s_name,role,*args):
        ''' add a person and allocate them a random room if he passes 'Y' as fouth paremeter'''
        if args:
            if args[0]=='Y':
                guy=Person(f_name,s_name,role)
                random_room=random.choice(list(self.rm_occupancy.keys()))

                self.rm_occupancy[random_room].append(guy.f_name)
                self.allocated_persons.append(guy.f_name)
            else:
                raise ValueError("value can only be Y")
        else:
            guy=Person(f_name,s_name,role)
            self.pending.append(guy.f_name)

    def reallocate_room(self, f_name,new_room_name):
        ''' gets the current room where person is alocated ; remove the person from that room and
        allocate the person to another room '''

        if f_name in self.persons == False:
            raise ValueError ("the person does not exist")
        if new_room_name not in self.rm_occupancy.keys() ==True:
            raise ValueError ("the room does not exist")

        for k,v in self.rm_occupancy.items():
            if f_name in v:
                v.remove(f_name)
        try:
            self.rm_occupancy[new_room_name].append(f_name) # add person to new room
        except:
            raise ValueError ("the room does not exist")


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
        super(LivingSpace, self).__init__(rm_name)
        self.rm_name=rm_name
        self.rm_size=6
