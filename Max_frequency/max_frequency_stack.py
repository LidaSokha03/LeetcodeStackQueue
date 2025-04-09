'''
Implement a stack that supports push, pop, and retrieving the maximum frequency element.
'''
class Stack:
    '''
    A simple stack implementation using a list
    '''
    def __init__(self):
        '''
        Initialize the stack
        '''
        self.items = []
        self.count = 0

    def push(self, value):
        '''
        Push an item onto the stack
        :param value: The item to push
        :return: None
        '''
        self.items.append(value)
        self.count += 1

    def pop(self):
        '''
        Pop an item from the stack
        :return: The popped item
        '''
        return self.items.pop()

    def isEmpty(self):
        '''
        Check if the stack is empty
        :return: True if empty, False otherwise
        '''
        return self.count == 0

    def peek(self):
        '''
        Peek at the top item of the stack without removing it
        :return: The top item
        '''
        if self.items != []:
            return self.items[-1]
        else:
            return None


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

class FreqStack:
    '''
    Implement a stack that supports push, pop, and retrieving the maximum frequency element.
    '''
    def __init__(self):
        '''
        Initialize the frequency stack.
        '''
        self.stack = Stack()
        self.queue = Queue()
        self.freq = dict()

    def push(self, value):
        '''
        Push an item onto the stack.
        :param value: The item to push.
        '''
        self.stack.push(value)
        if value not in self.freq:
            self.freq[value] = 1
        else:
            self.freq[value] += 1

    def pop(self):
        '''
        Pop the item with the maximum frequency from the stack.
        :return: The item with the maximum frequency.
        '''
        if self.stack.isEmpty():
            return None
        max_freq = max(self.freq.values())

        for i in range(len(self.stack.items) - 1, -1, -1):
            val = self.stack.items[i]
            if self.freq.get(val, 0) == max_freq:
                removed = self.stack.items.pop(i)
                self.stack.count -= 1
                self.freq[val] -= 1
                if self.freq[val] == 0:
                    del self.freq[val]
                return removed
        return None
