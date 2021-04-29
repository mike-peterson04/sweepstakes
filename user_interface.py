from contestant import Contestant
from sweepstakesstackmanager import SweepstakesStackManager
from sweepstakesqueuemanager import SweepstakesQueueManager


def generate_test_users():
    first_name = ['Liam', 'Noah', 'Jackson', 'Aiden', 'Elijah', 'Grayson', 'Lucas', 'Oliver',
                  'Caden', 'Mateo',	'Muhammad',	'Mason', 'Carter', 'Jayden', 'Ethan', 'Sebastian',
                  'James', 'Michael', 'Benjamin', 'Logan', 'Leo', 'Luca', 'Alexander', 'Levi', 'Daniel',
                  'Josiah', 'Henry', 'Jace', 'Julian', 'Jack', 'Ryan', 'Jacob', 'Asher', 'Wyatt', 'William',
                  'Owen', 'Gabriel', 'Miles', 'Lincoln', 'Ezra', 'Isaiah', 'Luke', 'Cameron', 'Caleb',
                  'Isaac', 'Carson', 'Samuel', 'Colton', 'Maverick', 'Matthew', 'Sophia', 'Olivia', 'Riley', 'Emma',
                  'Ava', 'Isabella', 'Aria', 'Aaliyah', 'Amelia', 'Mia', 'Layla', 'Zoe', 'Camilla', 'Charlotte',
                  'Eliana', 'Mila', 'Everly', 'Luna', 'Avery', 'Evelyn', 'Harper', 'Lily', 'Ella', 'Gianna',
                  'Chloe', 'Adalyn', 'Charlie', 'Isla', 'Ellie', 'Leah', 'Nora', 'Scarlett', 'Maya', 'Abigail',
                  'Madison', 'Aubrey', 'Emily', 'Kinsley', 'Elena', 'Paisley', 'Madelyn', 'Aurora', 'Peyton',
                  'Nova', 'Emilia', 'Hannah', 'Sarah',
                  'Ariana', 'Penelope', 'Lila']
    last_name = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez',
                 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor',
                 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez',
                 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright',
                 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera',
                 'Campbell', 'Mitchell', 'Carter', 'Roberts', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones',
                 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson',
                 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White',
                 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King',
                 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall',
                 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts']
    i = 1
    contestants = []
    while i <= 100:
        contestants.append(Contestant(first_name[i-1], last_name[i-1],
                                      f"{first_name[i-1]}.{last_name[i-1]}@hypothetical.com", i))
        i += 1
    return contestants


def text_print(to_print):

    i = 0
    while i < len(to_print):
        print(f"{to_print[i]}:{to_print[i+1]}")
        i += 2


def select_manager():

    print("press 1 for Stack Manager")
    print("press 2 for Queue Manager")
    while True:
        try:
            check = int(input())
            if check == 1:
                return SweepstakesStackManager()
            elif check == 2:
                return SweepstakesQueueManager()
            else:
                print("Please enter 1 or 2")
        except ValueError:
            print("Please enter 1 or 2")


def name_sweepstake():
    return input("What do you want to name this Sweepstake? ")


def notify_contestants(sweepstake, winner_id):
    # remove before submission this is a test process
    # sweepstake.temporary_test()
    count = 0
    while count < len(sweepstake.contestants):
        if sweepstake.contestants[count].registration_number == winner_id.registration_number:
            check = True
        else:
            check = False
        sweepstake.contestants[count].notify(check)
        count += 1


def bare_bones_front_end(creator, firm=None):
    # using dependence injection because I need to avoid circular imports
    # this requires a MarketingFirmCreator be passed in
    print("This Menu is primarily for testing purposes")
    print("While it is use able for all functionality")
    print("it is recommended you work with your marketing department to create a custom UI")
    print("________________________________________________________________________________")
    while True:
        print("Please select from the following options:")
        print("1: Create a new marketing firm and sweepstake manager")
        print("2: Create a new sweepstake and add users to it for an existing firm with no active sweepstakes")
        print("3: Create a new sweepstake or modify and existing sweepstake for a firm with active sweepstakes")
        print("4: Exit program")
        while True:
            try:
                i = int(input())
                if i == 1:
                    firm = all_creation_wrapper(creator)
                    print("New Firm Created")
                elif i == 2:
                    creation_wrapper(firm)
                    break
                elif i == 3:
                    sweepstake_management(firm)
                    break
                elif i == 4:
                    break
                else:
                    print("Invalid input please enter number from 1-4")
            except ValueError:
                print("Invalid input please enter number from 1-4")


def sweepstake_management(firm):
    # facade wrapper for working on existing marketing firms
    print("________________________________________________________________________")
    print("Please select what you want to do:")
    print("1: Add users to an existing sweepstake")
    print("2: Create a new sweepstake")
    print("3: Select a winner from a sweepstake")
    print("4: Return to previous menu")
    while True:
        try:
            i = int(input())
            if i == 1:
                sweepstake = select_sweepstake(firm)
                inject_users(sweepstake, select_user_type())
                firm.manager.insert_sweepstakes(sweepstake)
            elif i == 2:
                firm.create_sweepstakes()
                break
            elif i == 3:
                sweepstake = select_sweepstake(firm)
                notify_contestants(sweepstake, sweepstake.pick_winner())
            else:
                print("Invalid input please enter number from 1-3")
        except ValueError:
            print("Invalid input please enter number from 1-3")


def select_sweepstake(firm):
    sweepstake = firm.manager.get_sweepstakes()
    print(f"We have grabbed your Sweepstake {sweepstake.name}")
    print("is this the sweepstake you wish to use?(y/n)")
    check = input().upper()
    while True:
        if check == 'Y':
            return sweepstake
        elif check == 'N':
            firm.manager.insert_sweepstakes(sweepstake)
            check = input("Try again?(y/n) ").upper()
            if check == 'N':
                break
        else:
            print("invalid input please try again")


def creation_wrapper(firm):
    # this requires a MarketingFirm be passed in to implement a facade pattern
    firm.create_sweepstakes()
    contestants = select_user_type()
    firm.manager.insert_sweepstakes(inject_users(firm.manager.get_sweepstakes(), contestants))


def all_creation_wrapper(creator):
    # using dependence injection because I need to avoid circular imports
    # this requires a MarketingFirmCreator be passed in
    firm = creator.choose_manager_type()
    firm.create_sweepstakes()
    contestants = select_user_type()
    firm.manager.insert_sweepstakes(inject_users(firm.manager.get_sweepstakes(), contestants))
    return firm


def inject_users(sweepstake, contestants):
    # this is depending on receiving a sweepstake and a list of contestants
    # to make adding a lot of contestants to a single sweepstakes simple if you use my test generation function
    # or import from file
    for each in contestants:
        sweepstake.register_contestant(each)
    return sweepstake


def select_user_type():
    print("Press 1 to use pre generated users:")
    print("Press 2 to create your own users:")
    contestants = []
    while True:

        try:
            i = int(input())
            if i == 1:
                contestants = generate_test_users()
                break
            elif i == 2:
                contestants = create_users()
                break
            else:
                print("Please pick 1 or 2")
        except ValueError:
            print("Please pick 1 or 2")
        return contestants


def create_users():
    users = []
    print("How many users do you wish to create? ")
    while True:
        try:
            i = int(input())
            while i > 0:
                print(f"please enter the following information for contestant number {i}")
                print("What is their first name?:")
                first_name = input()
                print("What is their last name?:")
                last_name = input()
                print("What is their Email Address?:")
                email = input()
                users.append(Contestant(first_name, last_name, email, i))
                i -= 1
            break
        except ValueError:
            print("Please enter a number")

    return users
