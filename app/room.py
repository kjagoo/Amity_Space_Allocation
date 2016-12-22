from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

from .db_model import (Base, PersonDb, UnallocatedPerson, AllocatedPerson, AvailableRooms, RoomAllocations,
                          LivingSpaceAllocations, OfficeAllocations,DatabaseCreator)

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

    def add_person(self,f_name,s_name,role,wa=False):
        '''add person object to the persons list'''
        fullname = f_name + " " + s_name

        if role == 'FELLOW':
            person = Fellow(f_name,s_name)
            self.fellows.append(fullname)
        elif role == 'STAFF':
            person = Staff(f_name,s_name)
            self.staffs.append(fullname)
        else:
            raise TypeError("Person can only be Staff or Fellow")

        self.persons = self.staffs+self.fellows
        self.allocate_room(f_name,s_name,role,wa)
        print(fullname," successfully added ")

    def allocate_office_automatically(self,fullname):
        '''allocate everyone to an office automaticaly'''
        if (len(self.offices) > 0) and (len(self.available_rooms) > 0):
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

        if args[0]== 'Y' and role=="FELLOW":
            if (len(self.lspace) > 0):
                random_room = random.choice(list(set(self.available_rooms) & set(self.lspace)))

                if len(self.rm_occupancy[random_room]) < 4:
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

        if fullname not in self.persons:
            raise ValueError ("the person does not exist")
        if new_room_name not in self.rm_occupancy.keys():
            raise ValueError ("the room does not exist")
        if new_room_name in self.full_rooms:
            raise ValueError ("the room is full, kindly select another room")
        if new_room_name in self.offices:
            room_kind = self.offices
        elif new_room_name in self.lspace:
            room_kind = self.lspace
        try:
            old_room=[room for room in self.rm_occupancy.keys() if fullname in self.rm_occupancy[room] and room in room_kind][0]
            self.rm_occupancy[old_room].remove(fullname)
            if old_room in self.full_rooms: #check if previous room was full
                self.full_rooms.remove(old_room)# remove room from full room
                self.available_rooms.append(old_room)# make room available
        except:
            raise ValueError("Can only realocate rooms of same kind")
        try:
            self.rm_occupancy[new_room_name].append(fullname) # add person to new room
            print("Reallocate successfully to: ",new_room_name)
        except:
            raise ValueError ("the room does not exist in Room Occupancy dictionary")


    def print_room_allocated(self):
        '''prints a list of all alocated rooms and their occupance'''
        response = "List of Room Allocations"+ '\n'

        for k,v in self.rm_occupancy.items():
            if k in self.offices:
                kind="Office"
            else:
                kind="LivingSpace"

            response = response + kind + ' : ' + k+ '\n'
            response = response +  '-'*20+ '\n'
            response = response + ', '.join(self.rm_occupancy[k])+ '\n'
            response = response +  '-'*50 + '\n'

        print (response)

    def print_unallocated(self):
        response = " List Of Unallocated Persons "+ "\n"
        response = response + '-'*50+ "\n"
        print(response)
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
            response= "-"*50 + "\n"
            response = response + room_name + "\n"+ "\n"
            response = response + ', '.join(self.rm_occupancy[room_name])+ "\n"
            response= "-"*50 + "\n"
            print (response)
        else:
            raise TypeError("there is no such room, kindly try another name ")

    def save_state(self,db_name="default_db"):
        db = DatabaseCreator(db_name)
        Base.metadata.bind = db.engine
        db_session = db.session()

        for room in list(set(self.rooms) & set(self.lspace)):
            lspace_to_save = LivingSpaceAllocations(
                room_name=room,
                rm_type="LivingSpace")
            db_session.merge(lspace_to_save)

        for room in list(set(self.rooms) & set(self.offices)):
            office_to_save = OfficeAllocations(
                room_name=room,
                rm_type="Office")
            db_session.merge(office_to_save)

        for room in self.available_rooms:
            room_to_save = AvailableRooms(
                room_name=room)
            db_session.merge(room_to_save)

        for person in self.persons:
            if person in self.staffs:
                role="Staff"
            else:
                role="Fellow"

            person_to_save = PersonDb(
                name=person,
                role=role )
            db_session.merge(person_to_save)

        for person in self.unallocated_persons:
            person_to_save = UnallocatedPerson(
                name=person )
            db_session.merge(person_to_save)

        for person in self.allocated_persons:
            person_to_save = AllocatedPerson(
                name=person)
            db_session.merge(person_to_save)

        for room in self.rm_occupancy:
            members = ",".join(self.rm_occupancy[room])
            room_allocations = RoomAllocations(
                room_name=room,
                members=members)
            db_session.merge(room_allocations)

        db_session.commit()
        print("Success!")

    def load_state(self, dbname=None):
        """Loads data from a DB file into the app."""
        engine = create_engine("sqlite:///" + dbname + ".sqlite")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        people = session.query(PersonDb).all()
        allocated_persons = session.query(AllocatedPerson).all()
        unallocated_persons = session.query(UnallocatedPerson).all()
        rm_occupancy = session.query(RoomAllocations)
        available_rooms = session.query(AvailableRooms)
        lspaces = session.query(LivingSpaceAllocations)
        offices = session.query(OfficeAllocations)
        if not dbname:
            print("You must select a db to load.")
        else:
            for room in lspaces:
                self.rooms.append(room.room_name)
                self.lspace.append(room.room_name)

            for room in offices:
                self.rooms.append(room.room_name)
                self.offices.append(room.room_name)

            for person in people:
                if (person.role == "Staff"):
                    self.staffs.append(person.name)
                elif (person.role == "Fellow"):
                    self.fellows.append(person.name)
                self.persons = self.staffs + self.fellows

            for person in allocated_persons:
                self.allocated_persons.append(person.name)

            for person in unallocated_persons:
                self.unallocated_persons.append(person.name)
                
            for room in available_rooms:
                self.available_rooms.append(room.room_name)

            for occupancy in rm_occupancy:
                all_members = occupancy.members.split(",")
                self.rm_occupancy[occupancy.room_name] = all_members
            self.rm_occupancy.update(self.rm_occupancy)
            print (self.rm_occupancy)

            print("Data from %s loaded to the app." % dbname)

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
