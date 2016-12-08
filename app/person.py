#from docopt import docopt
class Person (object):

    def __init__(self,f_name,s_name,role):
        self.f_name=f_name
        self.s_name=s_name
        self.role=role



class Staff(Person):

    def __init__(self,f_name,s_name,role):
        super(Staff,self).__init__(f_name,s_name,role)
        self.f_name=f_name
        self.s_name=s_name
        self.role=role
        self.rm_type='Staff'

class Fellow(Person):

    def __init__(self,f_name,s_name,role):
        super(Fellow,self).__init__(f_name,s_name,role)
        self.f_name=f_name
        self.s_name=s_name
        self.role=role
        self.rm_type='LivingSpace','Office'
