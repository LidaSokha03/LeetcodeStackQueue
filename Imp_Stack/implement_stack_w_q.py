'''
Implement Stack using Queues
'''
class Queue:
    '''
    A simple queue implementation using a list.
    '''
    def __init__(self):
        '''
        Initialize the queue.
        '''
        self.items = []
        self.count = 0

    def enqueue(self, value):
        '''
        Add an item to the end of the queue.
        :param value: The item to add.
        '''
        self.items.append(value)
        self.count += 1

    def __len__(self):
        '''
        Get the number of items in the queue.
        :return: The number of items in the queue.
        '''
        return self.count

    def dequeue(self):
        '''
        Remove and return the first item from the queue.
        :return: The first item in the queue.
        '''
        self.count -= 1
        return self.items.pop(0)

    def is_empty(self):
        '''
        Check if the queue is empty.
        :return: True if the queue is empty, False otherwise.
        '''
        return not self.items

class MyStack:
    '''
    Implement a stack using two queues.
    '''
    def __init__(self):
        '''
        Initialize the stack.
        '''
        self.first_q = Queue()
        self.second_q = Queue()

    def push(self, value):
        '''
        Push an item onto the stack.
        :param value: The item to push.
        '''
        self.first_q.enqueue(value)

    def pop(self):
        '''
        Pop the top item off the stack.
        :return: The top item of the stack.
        '''
        result = None
        if self.first_q.count >= 1:
            while self.first_q.count > 1:
                self.second_q.enqueue(self.first_q.dequeue())
            result = self.first_q.dequeue()
            while not self.second_q.is_empty():
                self.first_q.enqueue(self.second_q.dequeue())
        return result

    def top(self) -> int:
        '''
        Get the top item of the stack without removing it.
        '''
        if not self.first_q.is_empty():
            return self.first_q.items[-1]
        return None


    def empty(self) -> bool:
        '''
        Check if the stack is empty.
        :return: True if the stack is empty, False otherwise.
        '''
        if len(self.first_q) == 0 and len(self.second_q) == 0:
            return True
        return False
