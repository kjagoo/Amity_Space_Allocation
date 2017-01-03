import unittest
# import sys
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
        len_offices=len(self.amity.offices)#previous length of office list
        len_rooms=len(self.amity.rooms)#previous length of rooms list
        uganda=self.amity.create_room('Tana','OFFICE')

        self.assertEqual(len(self.amity.offices),len_offices+1,msg='the room should be in the list of Offices ')
        self.assertEqual(len(self.amity.rooms),len_rooms+1,msg='the room should be in the list of room names')
        self.amity.create_room('burudi','LIVINGSPACE')
        self.assertIn('burudi',self.amity.lspace, msg='the room should be in the dictionary of rooms')

    def test_allocate_room(self):
        '''test if person is alocated the len(room) increases'''
        self.amity.create_room("hogs","office")
        len_allocated_persons=len(self.amity.allocated_persons)#previous list of persons allocated rooms
        len_unallocated_persons=len(self.amity.unallocated_persons)#previous list of persons unallocated_persons allocation
        self.amity.add_person('joshua','kagenyi','STAFF','N')
        self.assertEqual(len(self.amity.allocated_persons),len_allocated_persons+1,
        msg='person should be added to allocated list ')


    # def test_allocate_room_raises_error_on_wrong_fourth_paremeter(self):
    #     '''test value error raised for worng fourh paremeter'''
    #     with self.assertRaises(ValueError):self.amity.allocate_room('joshua','kagenyi','fellow','Z')

    def test_reallocation_room(self):
        ''' test wether person is reallocated successfully : remove from previous room and added to new room'''
        # automatically add person to room
        self.amity.create_room("tanzania","office")
        len_of_new_room=len(self.amity.rm_occupancy['tanzania'])#length of room before adding person

        self.amity.add_person('joshua','kagenyi','STAFF','N')
        print(self.amity.rm_occupancy)

        self.amity.reallocate_room('joshua kagenyi','tanzania')# check that lenght of new room has increased by 1
        self.assertEqual(len(self.amity.rm_occupancy['tanzania']),
        len_of_new_room+1,msg='number of occupants in new room should increase')

        person_in_room=[room for room in self.amity.rm_occupancy.keys() if 'joshua kagenyi'
                       in self.amity.rm_occupancy[room]]
                       # check that person exist in only one room
        self.assertEqual(len(person_in_room),1,
        msg='person should only exis in one room after reallocation ')

    def test_reallocation_room_raises_error_if_person_does_not_exist(self):
        ''' test that person being reallocated exists in Amity and ValueError raised if not'''
        with self.assertRaises(ValueError):self.amity.reallocate_room('joshua','banana_republic')

    def test_reallocation_room_raises_error_if_new_room_Not_exist(self):
        ''' Test new room exists in amity before realocation and assert valueerror raised if not'''
        with self.assertRaises(ValueError):self.amity.reallocate_room('justin_baiber','banana_republic')

    def test_number_of_room_occupants(self):
        '''Test that rooms have the right number of occupants'''
        for room in self.amity.rm_occupancy.keys():
            if room in self.amity.offices:
                self.assertTrue(len( self.amity.rm_occupancy[room])<=6)
            elif room in self.amity.lspace:
                self.assertTrue(len( self.amity.rm_occupancy[room])<=4)


    # def test_load_people(self):
    #     '''assert for every person in text file is loaded to persons list'''
    #     self.amity.load_people()
    #     with open('./people_to_load.txt', 'r') as people:
    #         for person in people:
    #             person=person.rstrip().split()
    #             self.assertIn(person[0],self.amity.persons)



if __name__ == '__main__':
    unittest.main()
