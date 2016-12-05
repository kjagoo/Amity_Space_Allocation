import unittest
import sys
sys.path.append('../')
from app.person import Person, Staff, Fellow

class TDDamity(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_person(self):
        joshua=Person('joshua','kagenyi','Fellow')
        joshua.add_person()
        result= joshua.person[0].f_name
        #Sprint (result)
        self.assertIn('joshua', result,msg='the room should be in the list of room names')

    def test_person_fello_in_list(self):
        Judo=Person('Judo','kagenyi','Fellow')
        Judo.add_person()
        result= Judo.fellow[0].f_name
        #print(result)
        self.assertIn('Judo', result ,msg='the person should be in the fellows list')

    def test_person_staff_in_list(self):
        joshua=Person('joshua','kagenyi','Staff')
        joshua.add_person()
        result= joshua.staff[0].f_name
        #print(result)
        self.assertIn('joshua', result ,msg='the person should be in the Staff list')



    '''def test_raise_error_on_wrong_role(self):
        hogs=Person('joshua','kagenyi','w')
        hogs.add_person()
        result= hogs.fellow
        self.assertIn('joshua', result ,msg='the person should be in the fellows list')'''



if __name__ == '__main__':
    unittest.main()
