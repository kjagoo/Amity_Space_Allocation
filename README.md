<img width="511" alt="screen shot 2017-01-03 at 11 17 09 am" src="https://cloud.githubusercontent.com/assets/8224798/21602573/5b55e73e-d1a6-11e6-95f0-ea994c60a3df.png">

**[# Installation](url)**

Clone the repo on github

`https://github.com/kjagoo/Amity_Space_Allocation`

Navigate to room folder

`cd amity`

Install requirements

`pip install -r requirements.txt`

**[Running the Program](url)**

`python main.py`

**[# Usage](url)**

1. `create_room <room_name> <room_type>..` creates a room where you provide a room name and a room type which can only be an office or living space. You can create as many rooms as possible where offices have a capacity of 6 while living spaces have a capacity of 4. 
 _> Example: create_room kenya office_ 
 
2. `add_person <first_name> <last_name> <role> [--wants_accomodation=N]` this adds people to amity program where w collect both the first and second name, the role which is either fellow or staff, and wether the person wants accomodation. Every person is automatically allocated an office as soon as is added while living spaces are only allocated to fellows on request. 
 _> Example: add_person john doe fellow --wants_accomodation=Y_ 
 
3. `reallocate_person <full_name> <new_room_name>` this command reallocates a person a room from the current occupancy. Reallocations are allowed only for rooms of same kind e.g office to office or living space to another living space. 
 _> Example: reallocate_person john doe kenya_ 
 
4. `load_people <filename>` this command loads a list of people in a text file to the program. The program reads line by line of the text file collection the first name, second name, role, wants_accomodation.
 _>  Example: load_people people_to_load.txt_
 
5. `print_allocations [--o=filename]` prints a lists of all allocations which is a list of rooms and occupants in each room. the method can also print into a text file with given information.
 
6. `print_unallocated [--o=filename]` prints a list of all unallocated persons. This list is populated when either all rooms are full or not available.The staff in this list are missing office spaces while the fellows could either be missing an office or living space or both.
 
7. `print_room <room_name>` this command prints out the occupants of the given room name: Example print_room Kenya.
 
8. `save_state [--db=sqlite_database]` this command saves the current state to an sqlite database with a given name. 
 _> Example: save_state --db=first_database_
 
9. `load_state [--db=sqlite_database]` this command allows you to load the state from the database and continue using the program from where you left off . 
 _> Example load_state --db=first_database_ 
 
10. `quit` this command closes down the program.
 
11. `-h, --help` this command gives a list of all available commands to help you navigate through the program. 

# **tests**
Run `nosetests --with-coverage --cover-erase --cover-package=test`

to capture the test coverage as well as perform a tests on the test files.

# **credits**
Joshua kagenyi
