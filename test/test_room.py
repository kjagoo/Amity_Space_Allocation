import unittest
#import sys
# sys.path.append('../')
from app.room import Amity, Room, Office, LivingSpace
from app.person import Person

class TDDamity(unittest.TestCase):
    def setUp(self):
        self.amity=Amity()

    def test_room_error_for_empty_parameters(self):
        '''test if error is raise when empty value is passed in Room'''
        with self.assertRaises(TypeError):
            Room()

    def test_raises_error_if_non_string_paremeters_passed(self):
        ''' Test that room captures only strings'''
        with self.assertRaises(TypeError):Room(123456)

    def test_amity_create_room_method(self):
        ''' test wether room object is added in list of rooms in Amity Class'''
        len_offices=len(self.amity.offices)#previous lenth of office list
        len_rooms=len(self.amity.rooms)#previous lenth of rooms list
        uganda=self.amity.create_room('uganda','Office')

        self.assertEqual(len(self.amity.rooms),len_offices+1,msg='the room should be in the list of Offices ')
        self.assertEqual(len(self.amity.rooms),len_rooms+1,msg='the room should be in the list of room names')
        tz=self.amity.create_room('tanzania','LivingSpace')
        self.assertIn('tanzania',self.amity.rm_occupancy, msg='the room should be in the dictionary of rooms')


    def test_allocate_room(self):
        len_allocated_persons=len(self.amity.allocated_persons)#previous list of persons allocated rooms
        len_unallocated_persons=len(self.amity.unallocated_persons)#previous list of persons unallocated_persons allocation
        self.amity.allocate_room('joshua','kagenyi','Fellow','Y')
        self.assertEqual(len(self.amity.allocated_persons),len_allocated_persons+1,msg='person should be added to allocated list ')

        self.amity.allocate_room('Judo','kagenyi','Fellow')
        self.assertEqual(len(self.amity.unallocated_persons),len_unallocated_persons+1,msg='the person should be added into the unallocated_persons list ')

    def test_allocate_room_raises_error_on_wrong_fourth_paremeter(self):
        '''test value error raised for worng fourh paremeter'''
        with self.assertRaises(ValueError):self.amity.allocate_room('joshua','kagenyi','Fellow','Z')

    def test_reallocation_room(self):
        ''' test wether person is reallocated successfully : remove from previous room and added to new room'''
        self.amity.rm_occupancy['uganda'].append('joshua') # automatically add person to room
        previous_room=[k for k, v in self.amity.rm_occupancy.items() if 'joshua' in v][0]
        len_previous_room=len(self.amity.rm_occupancy[previous_room])
        len_of_new_room=len(self.amity.rm_occupancy['tanzania'])

        self.amity.reallocate_room('joshua','tanzania')
        # check that lenght of new room has increased by 1
        self.assertEqual(len(self.amity.rm_occupancy['tanzania']),len_of_new_room+1,msg='number of occupants in new room should increase ')
        # check that length of previous room has decreased by 1
        self.assertEqual(len(self.amity.rm_occupancy[previous_room]),len_previous_room-1,msg='number of occupants in prevoius room should decrease ')

    def test_reallocation_room_raises_error_if_person_does_not_exist(self):
        ''' test that person being reallocated exists in Amity and ValueError raised if not'''
        with self.assertRaises(ValueError):self.amity.reallocate_room('joshua','banana_republic')

    def test_reallocation_room_raises_error_if_new_room_Not_exist(self):
        ''' Test new room exists in amity before realocation and assert valueerror raised if not'''
        with self.assertRaises(ValueError):self.amity.reallocate_room('justin_baiber','banana_republic')

    def test_print_allocation(self):
        self.amity.print_room_allocated()
        for person in self.amity.allocated_persons:
            self.assertTrue(any(person in people for people in self.amity.rm_occupancy.values()),msg='the report produced shorld include all alocated persons')

    def test_print_unallocated(self):
        self.amity.print_unallocated()
        


    # def test_room_office_in_instance(self):
    #     ''' test wether room instance gets the room size from Office Class'''
    #     hogs=Amity('hogs','Office')
    #     hogs.create_room()
    #     self.assertEqual(hogs.rm_name.rm_size, 6,msg='the room should be in the list of room names')
    #
    #
    # def test_room_LivingSpace_in_instance(self):
    #     ''' test wether instance has room type LivingSpace for room type living space'''
    #     hogs=Amity('hogs','LivingSpace')
    #     #print(hogs.rm_type)
    #     self.assertEqual('LivingSpace', hogs.rm_type,msg='the room should be in the list of room names')
    #
    #
    # def test_room_view_all_rooms(self):
    #     ''' view a list of rooms '''
    #     Uganda=Amity('uganda','LivingSpace')
    #     tanzania=Amity('Tanzania','LivingSpace')
    #     result=Uganda.create_room()
    #     result1=tanzania.create_room()
    #     #print (Uganda.rooms,Uganda.rooms.rm_name)
    #     self.assertIn('uganda',Uganda.rooms,msg='the room should be in the list of room names')
    #     self.assertIn('tanzania',tanzania.rooms,msg='the room should be in the list of room names')
    #
    # def test_add_person_in_room(self):
    #     ''' check if added person name is in room occupants list'''
    #     hogs=Amity('hogs','LivingSpace')
    #     hogs.create_room()
    #     joshua=Person('joshua','kagenyi','Fellow')
    #     joshua.add_person()
    #     hogs.allocate_room()
    #     #print(hogs.rm_occupancy[hogs.rm_name.rm_name],list(hogs.rm_occupancy.values()))
    #     self.assertIn(joshua.f_name.f_name, hogs.rm_occupancy[hogs.rm_name.rm_name], msg='the room should be in the list of room names')
    #
    # def test_print_all_rooms(self):
    #     '''prints a list of all rooms with their occupancy'''
    #     hogs=Amity('hogs','LivingSpace')
    #     hogs.allocate_room()
    #     hogs.view_all_rooms()
    #     print (hogs.rm_occupancy)
    #     self.assertIn('hogs', hogs.rm_occupancy, msg='the room should exist in dictionary of rooms')
    #
    #
    #
    # def test_room_space(self):
    #
    #     pass
    # def test_room_if_full_raises_value_error(self):
    #
    #     pass
    # def test_allocate_room(self):
    #
    #     pass
    #


if __name__ == '__main__':
    unittest.main()
