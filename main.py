'''
Usage:
    add_person <first_name> <last_name> <role> [--wants_accomodation=N]
    create_room <room_name> <room_type>
    reallocate_person <full_name> <new_room_name>
    load_people <filename>
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    print_room <room_name>
    save_state [--db=sqlite_database]
    load_state [--db=sqlite_database]
    quit
Options:
    -h, --help  Show this screen and exit
    -i --interactive  Interactive Mode

'''
from app.room import Amity
import sys
import cmd
import os
from termcolor import cprint, colored
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn
border = colored("*" * 20, 'cyan').center(80)

def introduction():
    print (border)
    print ("WELCOME TO AMITY SPACE ALLOCATION!".center(70))
    print(__doc__)
    print (border)

class AmityApplication(cmd.Cmd):
    cprint(figlet_format('AMITY', font='banner3-D'), 'cyan', attrs=['bold'])
    prompt = "Amity -->"
    amity=Amity()

    @docopt_cmd
    def do_create_room(self, arg):
        '''Usage: create_room <room_name> <room_type>'''
        r_name = arg["<room_name>"]
        r_type = arg["<room_type>"]
        if r_type.upper() not in ["OFFICE" , "LIVINGSPACE"]:

            print ('Wrong room type: can only be Office or LivingSpace')
        elif r_name.upper() in self.amity.rooms:
            print('Room already exists')
        else:
            self.amity.create_room(r_name.upper(), r_type.upper())

    @docopt_cmd
    def do_add_person(self, arg):
        '''Usage: add_person <firstname> <lastname> <role> [--wants_accomodation=N] '''
        f_name = arg["<firstname>"]
        l_name = arg["<lastname>"]
        role = arg["<role>"]
        wants_accomodation = arg["--wants_accomodation"]
        full_name = arg["<firstname>"] + " " + arg["<lastname>"]

        if full_name.upper()  in self.amity.persons:
            print ("Person already exists")
        else:
            try:
                self.amity.add_person(f_name.upper(), l_name.upper(), role.upper(),
                                      wants_accomodation)
            except TypeError:
                print ("error in add person syntax check for correct role i.e: fellow or Staff")
        # maybe work with the wants_accomodation upper in the amity function
    @docopt_cmd
    def do_load_people(self, arg):
        ''' Usage: load_people <filename>'''
        file_n = arg["<filename>"]
        try:
            self.amity.load_people(file_n)
        except Exception:
            print("Error processing file")
            # Either make this a global response for any type of error
            # or customize for each type of error that might occur

    @docopt_cmd
    def do_reallocate_person(self, arg):
        ''' Usage: reallocate_person <firstname> <lastname> <new_room_name>'''
        first_name = arg["<firstname>"]
        last_name = arg["<lastname>"]
        full_name = arg["<firstname>"] + " " + arg["<lastname>"]
        new_room = arg["<new_room_name>"]
        if full_name.upper() not in self.amity.persons:
            print ("Person does not exist in amity")
        elif new_room.upper() in self.amity.rooms:
            try:
                self.amity.reallocate_room(full_name.upper(), new_room.upper())
            except ValueError:
                print(" can only reallocate room of same kind")

        else:
            print("The room does not exist in amity")

    @docopt_cmd
    def do_print_room(self, arg):
        ''' Usage: print_room <room_name>'''
        r_name = arg["<room_name>"]
        if r_name.upper() in self.amity.rooms:
            self.amity.print_room_occupants(r_name.upper())
        else:
            print('There is no room called %s in Amity' % r_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        '''Usage: print_allocations [--o=filename] '''
        filename = arg["--o"]
        if filename:
            self.amity.print_room_allocated(filename)
        else:
            self.amity.print_room_allocated()

    @docopt_cmd
    def do_print_unallocated(self, arg):
        '''Usage: print_unallocated [--o=filename] '''
        filename = arg["--o"]
        if filename:
            self.amity.print_unallocated(filename)
        else:
            self.amity.print_unallocated()

    @docopt_cmd
    def do_save_state(self, arg):
        '''Usage: save_state [--db=sqlite_database]'''
        database_name = arg["--db"] or ""
        self.amity.save_state(database_name)

    @docopt_cmd
    def do_load_state(self, arg):
        '''Usage: load_state [--db=sqlite_database]'''
        try:
            self.amity.load_state(arg["--db"])
        except Exception:
            print("Error loading file")

    @docopt_cmd
    def do_quit(self, arg):
        '''Usage: quit '''
        print("GOODBYE!!!")
        exit()
if __name__ == '__main__':
    introduction()
    AmityApplication().cmdloop()
