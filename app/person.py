#from docopt import docopt
class Person (object):

    def __init__(self,f_name,s_name):
        self.f_name=f_name
        self.s_name=s_name
        self.fullname=f_name + " " + s_name


class Staff(Person):

    def __init__(self,f_name,s_name):
        super(Staff,self).__init__(f_name,s_name)
        self.f_name=f_name
        self.s_name=s_name
        self.fullname=f_name + " " + s_name
        self.rm_type='OFFICE'

class Fellow(Person):

    def __init__(self,f_name,s_name):
        super(Fellow,self).__init__(f_name,s_name)
        self.f_name=f_name
        self.s_name=s_name
        self.fullname=f_name + " " + s_name
        self.rm_type='LIVINGSPACE','OFFICE'
