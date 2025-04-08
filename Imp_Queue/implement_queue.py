'''
Implementing a queue using two stacks
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


class MyQueue:
    '''
    Implementing a queue using two stacks
    '''
    def __init__(self):
        '''
        Initialize the queue
        '''
        self.first = Stack()
        self.second = Stack()

    def push(self, x: int) -> None:
        '''
        Push an item onto the queue
        :param x: The item to push
        :return: None
        '''
        self.first.push(x)

    def pop(self) -> int:
        '''
        Pop an item from the queue
        :return: The popped item
        '''
        result = None
        if self.first:
            while self.first.items:
                self.second.push(self.first.pop())
            result =  self.second.pop()
            while self.second.items:
                self.first.push(self.second.pop())
        return result

    def peek(self) -> int:
        '''
        Peek at the front item of the queue without removing it
        :return: The front item
        '''
        result = None
        if self.first.items:
            while self.first.items:
                self.second.push(self.first.pop())
            result = self.second.peek()
            while self.second.items:
                self.first.push(self.second.pop())
        return result

    def empty(self) -> bool:
        '''
        Check if the queue is empty
        :return: True if empty, False otherwise
        '''
        if not self.first.items and not self.second.items:
            return True
        return False
