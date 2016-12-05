from .person import Person
#from docopt import docopt
#print (docopt(__doc__))
class Amity(object):
    ''' amity class creates multiple rooms and allocates to persons'''

    def __init__(self,rm_name,*args):
        self.rm_name=rm_name
        self.rm_size=0

        if len(args)>0:
            self.rm_type=args[0]
        else:
            raise TypeError ('add room type')

        self.offices=['uganda','nigeria']
        self.lspace=['kenya','tanzania']
        self.rooms=self.offices +self.lspace
        self.fellows=['joshua','jones','maria','daniels']
        self.staff=['abby','dan','chris','jack']
        self.person=self.staff+self.fellows
        self.rm_occupancy={}
        self.pending=[]

    def create_room(self):
        if self.rm_name ==' ':
            raise TypeError ('Room name should not be empty')

        if isinstance(self.rm_name,str)==False:
            raise TypeError ('Room name should be a string')

        self.rm_name=Room(self.rm_name,self.rm_type)
        self.rm_size=Room(self.rm_name,self.rm_type).rm_size
        self.rooms.append(self.rm_name.rm_name)
        self.rm_occupancy={self.rm_name.rm_name:[]}
        if (self.rm_name.rm_name) in self.rooms: self.rooms.remove(self.rm_name.rm_name) #remove similar

        #print (self.rm_occupancy)

    def allocate_room(self):

        for room in self.rooms:
            self.rm_occupancy[room]=[]
        self.rm_occupancy[self.rm_name]=[]

        count=0
        ee={office:self.rm_occupancy[office] for office in set(self.rm_occupancy.keys()) & set(self.offices)}
        print (ee)
        for office in ee:
            for person in self.person:
                if len(self.rm_occupancy[office])< 6:
                    self.rm_occupancy[office].append(person)
                    
                else:
                    self.pending.append(person)
                    count+=1

        for lspace in sorted(self.rm_occupancy.keys()):
            for person in self.fellows:
                if len(self.rm_occupancy[lspace])< 4:
                    self.rm_occupancy[lspace].append(person)
                    self.person.remove(person)
                else:
                    self.pending.append(person)
                    count+=1

        #print (self.rm_occupancy)
        #print (self.pending,'pending allocation')

    def reallocate_room(self):
        pass

    def view_all_rooms(self):
        print ('List of all rooms',self.rm_occupancy)

    def print_room(self):
        print ('List of all occupants in room',self.rm_occupancy[rm_name])

    def print_unallocated(self):
        print ('List of all unallocated persons',self.pending)

    def load_people(self):
        pass


class Room (Amity):
    ''' Room class creates the object attributes of the room'''
    def __init__(self, rm_name, *args):
        super(Room,self).__init__(rm_name,*args)
        self.rm_name=rm_name
        self.occupants=[]
        self.rm_size=0

        if self.rm_type=='Office':
            self.rm_size = Office().rm_size

        elif self.rm_type =='LivingSpace':
            self.rm_size = LivingSpace().rm_size
        else:
            raise ValueError ('Rooms can only be LivingSpace or Offices')

class Office(Room):

    def __init__(self):
        self.rm_size=6

class LivingSpace(Room):
    def __init__(self):
        self.rm_size=6
