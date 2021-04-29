from data_queue import Queue


class SweepstakesQueueManager:
    def __init__(self):
        self.stack = Queue()

    def insert_sweepstakes(self, sweepstakes):
        self.stack.enqueue(sweepstakes)

    def get_sweepstakes(self):
        result = self.stack.dequeue()
        return result
