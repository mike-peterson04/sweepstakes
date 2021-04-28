class Contestant:

    def __init__(self, first_name, last_name, email, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.registration_number = registration_number
        self.email = email

    def notify (self, is_winner):
        pass