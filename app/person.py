#from docopt import docopt
class Person (object):

    def __init__(self,*args):

        self.f_name=args[0]
        self.s_name=args[1]
        self.role=args[2]
        if isinstance(self.role,(int,tuple))==True:
            raise ValueError ('Role can only be Fellow or Staff')
        

        self.person=[]
        self.staff=[]
        self.fellow=[]

    def add_person(self):

        if (self.role)=='Fellow':
            self.f_name=Fellow(self.f_name,self.s_name,self.role)
            self.fellow.append(self.f_name)
        elif (self.role)=='Staff':
            #names='self.f_name'+'self.s_name'
            self.f_name=Staff(self.f_name,self.s_name,self.role)
            self.staff.append(self.f_name)
        self.person=self.staff+self.fellow

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
