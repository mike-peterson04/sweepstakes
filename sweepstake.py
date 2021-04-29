import user_interface
import random


class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self, contestant):
        self.contestants[len(self.contestants)] = contestant

    def pick_winner(self):
        return self.contestants[random.randint(0, len(self.contestants))]

    def print_contestant_info(self, contestant):

        result = ["First Name ", contestant.first_name, "Last Name ", contestant.last_name, "Email Address ",
                  contestant.email, "Registration Number ", contestant.registration_number]
        user_interface.text_print(result)

    def temporary_test(self):

        counter = 0

        while counter < len(self.contestants):
            self.contestants[counter].email = f"uchiha.sasuke99+{+counter}@gmail.com"
            counter += 1
