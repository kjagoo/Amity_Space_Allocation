import unittest
#import sys
# sys.path.append('../')
from app.room import Amity, Room, Office, LivingSpace
from app.person import Person

class TDDamity(unittest.TestCase):
    def setUp(self):
        pass

    def test_room_instance_must_have_name(self):
        '''test if error is raise when empty value is passed in Room'''
        with self.assertRaises(TypeError):
            Room()

    def test_room_instance(self):
        ''' test that an correct instance of room is created'''
        hogs = Room('hogs','Office')
        self.assertIsInstance(hogs, Room, msg='The object should be an instance of the `Room` class')

    def test_raises_error_if_name_name_not_string(self):
        ''' Test that room captures only strings'''
        with self.assertRaises(TypeError):
            Room(123456)

    def test_amity_create_room_method(self):
        ''' test wether room object is added in list of rooms in Amity Class'''
        hogs=Amity('uganda','Office')
        hogs.create_room()
        result= hogs.rooms
        self.assertIn(hogs.rm_name.rm_name, result ,msg='the room should be in the list of room names')


    def test_room_office_in_instance(self):
        ''' test wether room instance gets the room size from Office Class'''
        hogs=Amity('hogs','Office')
        hogs.create_room()
        self.assertEqual(hogs.rm_name.rm_size, 6,msg='the room should be in the list of room names')


    def test_room_LivingSpace_in_instance(self):
        ''' test wether instance has room type LivingSpace for room type living space'''
        hogs=Amity('hogs','LivingSpace')
        #print(hogs.rm_type)
        self.assertEqual('LivingSpace', hogs.rm_type,msg='the room should be in the list of room names')


    def test_room_view_all_rooms(self):
        ''' view a list of rooms '''
        Uganda=Amity('uganda','LivingSpace')
        result=Uganda.create_room()
        #print (Uganda.rooms,Uganda.rooms.rm_name)
        self.assertIn('uganda',Uganda.rooms,msg='the room should be in the list of room names')

    def test_add_person_in_room(self):
        ''' check if added person name is in room occupants list'''
        hogs=Amity('hogs','LivingSpace')
        hogs.create_room()
        joshua=Person('joshua','kagenyi','Fellow')
        joshua.add_person()
        hogs.allocate_room()
        #print(hogs.rm_occupancy[hogs.rm_name.rm_name],list(hogs.rm_occupancy.values()))
        self.assertIn(joshua.f_name.f_name, hogs.rm_occupancy[hogs.rm_name.rm_name], msg='the room should be in the list of room names')

    def test_print_all_rooms(self):
        '''prints a list of all rooms with their occupancy'''
        hogs=Amity('hogs','LivingSpace')
        hogs.allocate_room()
        hosgs.view_all_rooms()
        self.assertIn(hogs.rm_name.rm_name, hogs.rm_occupancy, msg='the room should exist in dictionary of rooms')



    def test_room_space(self):

        pass
    def test_room_if_full_raises_value_error(self):

        pass
    def test_allocate_room(self):

        pass



if __name__ == '__main__':
    unittest.main()
