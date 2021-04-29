from data_stack import Stack


class SweepstakesStackManager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)

    def get_sweepstakes(self):
        result = self.stack.pop()
        return result
