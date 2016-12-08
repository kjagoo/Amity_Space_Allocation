import unittest
import sys
sys.path.append('../')
from app.person import Person, Staff, Fellow
from app.room import Amity

class TDDamity(unittest.TestCase):
    def setUp(self):
        self.amity=Amity()

    def test_add_person(self):
        prev_len_persons=len(self.amity.persons)#length of list of persons before adding a person
        prev_len_fellows=len(self.amity.fellows)#length of list of fellows before adding a fellow
        prev_len_staffs=len(self.amity.staffs)#ength of list of staffs before adding a staff

        joshua=self.amity.add_person('Judo','kagenyi','Fellow')


        self.assertEqual(len(self.amity.persons), prev_len_persons+1,msg='The list of persons should increase')
        self.assertEqual(len(self.amity.fellows), prev_len_fellows+1,msg='The list of fellows should increase')
        self.assertEqual(self.amity.fellows[0].role, "Fellow",msg='the Person create Should be a Fellow')

        joshua=self.amity.add_person('Joshua','kagenyi','Staff')

        self.assertEqual(len(self.amity.staffs), prev_len_staffs+1,msg='The list of staffs should increase')
        self.assertEqual(self.amity.staffs[0].role, "Staff",msg='the Person create Should be a Staff')



    #

    def test_raise_error_on_wrong_role(self):
        pass


if __name__ == '__main__':
    unittest.main()
