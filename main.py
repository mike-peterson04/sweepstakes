from contestant import Contestant


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
    while i >= 100:
        contestants.append(Contestant(first_name[i-1], last_name[i-1],
                                      f"{first_name[i-1]}.{last_name[i-1]}@hypothetical.com", i))
        i += 1
    return contestants


def run_simulation():
    contestants = generate_test_users()


if __name__ == '__main__':
    run_simulation()
