from .person import Person, Fellow, Staff
import random
# import os
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
        self.rm_occupancy={'uganda':['joshua','Robert'],'tanzania':['job']}
        self.unallocated_persons=['joshua','job']
        self.allocated_persons=['joshua','job']

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
            self.unallocated_persons.append(guy.f_name)

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


    def print_room_allocated(self):
        '''prints a list of all alocated rooms and their occupance'''
        for person in self.allocated_persons:
            room_name=[k for k, v in self.rm_occupancy.items() if person in v ][0]
            return ('Room : ',room_name, ' = ', ', '.join(self.rm_occupancy[room_name]),'\n')


    def print_unallocated(self):
        person=0
        for person in self.unallocated_persons:
            return (person)

    def load_people(self):
        '''get names of people from a list and randomly allocate them rooms'''
        f = open('./people_to_load.txt', 'r')
        people = f.read().split(',')
        people=[people.rstrip('\n') for people in open('./people_to_load.txt')]

        for person in people:
            random_room=random.choice(list(self.rm_occupancy.keys()))
            self.rm_occupancy[random_room].append(person)
        return(self.rm_occupancy)

    def print_room_occupants(self,room_name):
        '''prints out all the occupants of the said room'''
        if room_name in list(self.rm_occupancy.keys()):
            return (room_name,': ', ', '.join(self.rm_occupancy[room_name]))
        else:
            raise TypeError("there is no such room, kindly try another name ")




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
