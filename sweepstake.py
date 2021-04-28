import user_interface
import random


class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self,contestant):
        self.contestants[len(self.contestants)] = contestant

    def pick_winner(self):
        pass

    def print_contestant_info(self,contestant):
        pass