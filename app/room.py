from .person import Person, Fellow, Staff
import random
# import os
#from docopt import docopt
#print (docopt(__doc__))
class Amity(object):
    ''' amity class creates multiple rooms and allocates to persons'''

    def __init__(self):
        self.offices=['tanzania','uganda']
        self.lspace=['kenya']
        self.rooms=self.offices +self.lspace
        self.fellows=[]
        self.staffs=[]
        self.persons=self.staffs+self.fellows
        self.rm_occupancy={'uganda':['Robert'],'tanzania':['job'],'kenya':[]}
        self.unallocated_persons=['job']
        self.allocated_persons=['joshua','job']
        self.available_rooms=self.rooms
        self.full_rooms=[]

    def create_room(self,rm_name,rm_type):
        '''create a room instance and append it to the rooms lists.'''

        if rm_name in self.rooms:
            raise ValueError("A room with same name already exist")
        if rm_type=='Office':
            rm_name=Office(rm_name)
            self.offices.append(rm_name.rm_name)

        elif rm_type=='LivingSpace':
            rm_name=LivingSpace(rm_name)
            self.lspace.append(rm_name.rm_name)

        self.rooms=self.offices +self.lspace
        self.rm_occupancy[rm_name.rm_name]=[]


    def add_person(self,f_name,s_name,role,*args):
        '''add person object to the persons list'''

        fullname=f_name+s_name
        if role=='Fellow':
            f_name=Fellow(f_name,s_name,role)
            self.fellows.append(f_name.f_name)
        elif role=='Staff':
            f_name=Staff(f_name,s_name,role)
            self.staffs.append(f_name.f_name)
        else:
            raise TypeError("Person can only be Staff or Fellow")

        self.persons=self.staffs+self.fellows


    def allocate_office_automatically(self,f_name):
        '''allocate everyone to an office automaticaly'''
        random_room=random.choice(self.available_rooms)
        if random_room in self.offices:# get random office
            self.rm_occupancy[random_room].append(f_name)
            if len(self.rm_occupancy[random_room])==6:
                self.full_rooms.append(random_room)
                self.available_rooms.remove(random_room)
        else:
            self.unallocated_persons.append(f_name)

    def allocate_room(self,f_name,s_name,role,*args):
        ''' add a person and allocate them a random room if he passes 'Y' as fouth paremeter'''
        if args:
            if args[0]=='Y':
                guy=Person(f_name,s_name,role)
                self.allocated_persons.append(guy.f_name)#add person to list of persons with rooms
                self.allocate_office_automatically(guy.f_name)# allocate office automaticaly
                random_room=random.choice(self.available_rooms)
                if random_room in self.lspace:
                    self.rm_occupancy[random_room].append(guy.f_name)#add person to living space room
                    if len(self.rm_occupancy[random_room])==4:
                        self.full_rooms.append(random_room)
                        self.available_rooms.remove(random_room)
            elif args[0]=='N':
                guy=Person(f_name,s_name,role)
                self.unallocated_persons.append(guy.f_name)
                self.allocate_office_automatically(guy.f_name)
            else:
                raise ValueError("value can only be Y or N")
        else:
            guy=Person(f_name,s_name,role)
            self.allocate_office_automatically(guy.f_name)

    def reallocate_room(self, f_name,new_room_name):
        ''' gets the current room where person is alocated ; remove the person from that room and
        allocate the person to another room '''

        if f_name in self.persons == False:
            raise ValueError ("the person does not exist")
        if new_room_name not in self.rm_occupancy.keys() ==True:
            raise ValueError ("the room does not exist")
        if new_room_name in self.full_rooms ==True:
            raise ValueError ("the room is full, kindly select another room")

        for k,v in self.rm_occupancy.items():#remove person from curret room occupancy
            if f_name in v:
                v.remove(f_name)
                if k in self.full_rooms: #check if previous room was full
                    self.full_rooms.remove(k)# remove room from full room
                    self.available_rooms.append(k)# make room available
        try:
            self.rm_occupancy[new_room_name].append(f_name) # add person to new room
        except:
            raise ValueError ("the room does not exist in Room Occupancy dictionary")

    def print_room_allocated(self):
        '''prints a list of all alocated rooms and their occupance'''
        for k,v in self.rm_occupancy.items():
            for person in self.allocated_persons:
                if person in v:
                    return ('Room : ',k, ' = ', ', '.join(self.rm_occupancy[k]),'\n')

    def print_unallocated(self):
        for person in self.unallocated_persons:
            return (person)

    def load_people(self):
        '''get names of people from a txt file and randomly allocate them rooms'''
        with open('./people_to_load.txt', 'r') as people:
            for person in people:
                person=person.rstrip().split()
                accomodate = person[3] if len(person) == 4 else "N"
                self.add_person(person[0], person[1], person[2])
                self.allocate_room(person[0], person[1], person[2],
                                 accomodate)
        print (self.persons)

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

    def __init__(self,rm_name):
        super(Office, self).__init__(rm_name)
        self.rm_name=rm_name
        self.rm_size=6


class LivingSpace(Room):

    def __init__(self,rm_name):
        super(LivingSpace, self).__init__(rm_name)
        self.rm_name=rm_name
        self.rm_size=6
