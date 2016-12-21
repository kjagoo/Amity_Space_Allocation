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
        self.rm_occupancy={}
        self.unallocated_persons=[]
        self.allocated_persons=[]
        self.available_rooms=self.rooms
        self.full_rooms=[]

    def create_room(self,rm_name,rm_type):
        '''create a room instance and append it to the rooms lists.'''
        rm_type = rm_type.upper()
        mapping = {'OFFICE': Office, 'LIVINGSPACE': LivingSpace}
        new_room = mapping[rm_type](rm_name)

        if rm_type == 'OFFICE':
            self.offices.append(new_room.rm_name)
        elif rm_type=='LIVINGSPACE':
            self.lspace.append(new_room.rm_name)

        self.rooms=self.offices +self.lspace
        self.available_rooms.append(new_room.rm_name)
        self.rm_occupancy[new_room.rm_name]=[]
        print (new_room.rm_name,"Room successfully created")

    def add_person(self,f_name,s_name,role,*args):
        '''add person object to the persons list'''
        fullname = f_name + " " + s_name

        if len(args) == 0:
            args = "N"

        if role == 'FELLOW':
            person = Fellow(f_name,s_name)
            self.fellows.append(fullname)
        elif role == 'STAFF':
            person = Staff(f_name,s_name)
            self.staffs.append(fullname)
        else:
            raise TypeError("Person can only be Staff or Fellow")

        self.persons = self.staffs+self.fellows
        self.allocate_room(f_name,s_name,role,args[0])
        print(fullname," successfully added")

    def allocate_office_automatically(self,fullname):
        '''allocate everyone to an office automaticaly'''
        if len(self.offices)>0:
            random_room = random.choice(list(set(self.available_rooms) & set(self.offices)))
            if len(self.rm_occupancy[random_room]) < 6:# get random office
                self.rm_occupancy[random_room].append(fullname)
                print ("successfully alocated office")
            elif len(self.rm_occupancy[random_room]) == 6:
                self.full_rooms.append(random_room)
                self.available_rooms.remove(random_room)

            else:
                self.unallocated_persons.append(fullname)
        else:
            self.unallocated_persons.append(fullname)


    def allocate_room(self,f_name,s_name,role,*args):
        ''' add a person and allocate them a random room if he passes 'Y' as fouth paremeter'''
        guy=Person(f_name,s_name)

        if args[0] == 'Y' and role == "FELLOW":
            if (len(self.lspace) > 0):
                random_room = random.choice(list(set(self.available_rooms) & set(self.lspace)))
                for room in list(set(self.available_rooms) & set(self.lspace)):
                    if guy.fullname in self.rm_occupancy[room]:
                        break

                if len(self.rm_occupancy[random_room]) < 5:
                    self.rm_occupancy[random_room].append(guy.fullname)#add person to living space room
                    self.allocated_persons.append(guy.fullname)#add person to list of persons with rooms
                elif len(self.rm_occupancy[random_room]) == 4:
                    self.full_rooms.append(random_room)
                    self.available_rooms.remove(random_room)

                self.allocate_office_automatically(guy.fullname)
            else:
                self.unallocated_persons.append(guy.fullname)


        else:
            self.unallocated_persons.append(guy.fullname)
            self.allocate_office_automatically(guy.fullname)
        

    def reallocate_room(self, fullname,new_room_name):
        ''' gets the current room where person is alocated ; remove the person from that room and
        allocate the person to another room '''

        if fullname in self.persons == False:
            raise ValueError ("the person does not exist")
        if new_room_name not in self.rm_occupancy.keys() ==True:
            raise ValueError ("the room does not exist")
        if new_room_name in self.full_rooms ==True:
            raise ValueError ("the room is full, kindly select another room")

        for k,v in self.rm_occupancy.items():#remove person from curret room occupancy
            if fullname in v:
                v.remove(fullname)
                if k in self.full_rooms: #check if previous room was full
                    self.full_rooms.remove(k)# remove room from full room
                    self.available_rooms.append(k)# make room available
        try:
            self.rm_occupancy[new_room_name].append(fullname) # add person to new room
            print("Reallocate successfully to: ",new_room_name)
        except:
            raise ValueError ("the room does not exist in Room Occupancy dictionary")


    def print_room_allocated(self):
        '''prints a list of all alocated rooms and their occupance'''
        print ("List of Room Allocations")
        for k,v in self.rm_occupancy.items():
            if k in self.offices:
                kind="Office"
            if k in self.lspace:
                kind="LivingSpace"
            print (kind,' : ',k )
            print('-'*20)
            print (', '.join(self.rm_occupancy[k]))
            print('-'*50)

    def print_unallocated(self):
        print(" List Of Unallocated Persons ")
        print('-'*50)
        count=1
        for person in self.unallocated_persons:
            print (count,":",person)
            count+=1


    def load_people(self, filepath):
        '''get names of people from a txt file and randomly allocate them rooms'''
        with open(filepath, 'r') as people:
            for person in people:
                person_details = person.rstrip().split()
                accomodate = person_details[3] if len(person_details) == 4 else "N"
                self.add_person(person_details[0], person_details[1],
                                person_details[2],accomodate)

        print (self.persons)

    def print_room_occupants(self,room_name):
        '''prints out all the occupants of the said room'''
        if room_name in list(self.rm_occupancy.keys()):
            print("-"*50)
            print (room_name,' : ')
            print( ', '.join(self.rm_occupancy[room_name]))
            print("-"*50)
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
