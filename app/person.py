#from docopt import docopt
class Person (object):

    def __init__(self,*args):


        self.persons=[]
        self.staffs=[]
        self.fellows=[]

    def add_person(self,f_name,s_name,role):

        if role=='Fellow':
            f_name=Fellow(f_name,s_name,role)
            self.fellows.append(f_name)
        elif self.role=='Staff':
            f_name=Staff(f_name,s_name,role)
            self.staffs.append(f_name)
        self.persons=self.staffs+self.fellows

class Staff(Person):

    def __init__(self,f_name,s_name,role,*args):
        super(Staff,self).__init__(f_name,s_name,role,*args)
        self.f_name=f_name
        self.s_name=s_name
        self.role=role
        self.rm_type='Office'

class Fellow(Person):

    def __init__(self,f_name,s_name,role,*args):
        super(Fellow,self).__init__(f_name,s_name,role,*args)
        self.f_name=f_name
        self.s_name=s_name
        self.role=role
        self.rm_type='LivingSpace','Office'
