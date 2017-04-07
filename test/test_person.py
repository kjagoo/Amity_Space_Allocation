import unittest
import sys
sys.path.append('../')
from app.person import Person, Staff, Fellow
from app.room import Amity

class TDDamity(unittest.TestCase):
    def setUp(self):
        self.amity=Amity()

    def test_add_person(self):
        ''' Test create a person and his role (staff or fellow)'''
        prev_len_persons=len(self.amity.persons)#length of list of persons before adding a person
        prev_len_fellows=len(self.amity.fellows)#length of list of fellows before adding a fellow
        prev_len_staffs=len(self.amity.staffs)#length of list of staffs before adding a staff

        joshua=self.amity.add_person('Judo','kagenyi','FELLOW','Y')

        self.assertEqual(len(self.amity.persons), prev_len_persons+1,msg='The list of persons should increase')
        self.assertEqual(len(self.amity.fellows), prev_len_fellows+1,msg='The list of fellows should increase')

        joshua=self.amity.add_person('Joshua','kagenyi','STAFF','N')
        self.assertEqual(len(self.amity.staffs), prev_len_staffs+1,msg='The list of staffs should increase')


    def test_raise_error_on_wrong_role(self):
        '''test error is raised if person is not staff or Fellow'''
        with self.assertRaises(TypeError):self.amity.add_person('Joshua','kagenyi','teacher','y')






if __name__ == '__main__':
    unittest.main()
