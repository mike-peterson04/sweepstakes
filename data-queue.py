class Queue:
    """This .py file cannot be named 'queue', as the debugger will confuse it with its own queue"""

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
