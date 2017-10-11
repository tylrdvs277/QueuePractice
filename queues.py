# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 3
# Term:        Fall 2017

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class QueueLinked:

    def __init__(self, capacity):
        # Creates an empty queue with a capacity
        self.capacity = capacity
        self.num_items = 0
        self.front = None
        self.end = None

    def is_empty(self):
        # Returns true if the queue is empty and false otherwise
        return (self.num_items == 0)

    def is_full(self):
        # Returns true if the queue is full and false otherwise
        return (self.num_items == self.capacity)

    def num_in_queue(self):
        # Returns the size of the queue
        return self.num_items

    def enqueue(self, item):
        # Adds an item to the end of the queue if not full 
        # and raises an error otherwise
        if self.is_full():
            raise IndexError
        elif self.is_empty():
            self.front = self.end = Node(item)
        else:
            temp = Node(item)
            self.end.set_next(temp)
            self.end = temp
        self.num_items += 1

    def dequeue(self):
        # Removes and returns item from the front of the queue if not empty
        # and raises an error otherwise
        if self.is_empty():
            raise IndexError
        elif self.num_items == 1:
            data = self.front.get_data()
            self.front = self.end = None
        else:
            data = self.front.get_data()
            self.front = self.front.get_next()
        self.num_items -= 1
        return data


class QueueArray:

    def __init__(self, capacity):
        # Creates an empty queue with a capacity
        self.capacity = capacity
        self.num_items = self.enqueue_idx = self.dequeue_idx = 0
        self.items = [None] * capacity

    def is_empty(self):
        # Returns true if the queue is empty and false otherwise
        return (self.num_items == 0)

    def is_full(self):
        # Returns true if the queue is full and false otherwise
        return (self.num_items == self.capacity)

    def num_in_queue(self):
        # Returns size of the queue
        return self.num_items

    def enqueue(self, item):
        # Adds an item to the end of the queue if not full 
        # and raises an error otherwise
        if self.is_full():
            raise IndexError
        else:
            self.items[self.enqueue_idx] = item
            self.enqueue_idx = (self.enqueue_idx + 1) % self.capacity
            self.num_items += 1

    def dequeue(self):
        # Removes and returns item from the front of the queue if not empty
        # and raises an error otherwise
        if self.is_empty():
            raise IndexError
        else:
            temp = self.items[self.dequeue_idx]
            self.items[self.dequeue_idx] = None
            self.dequeue_idx = (self.dequeue_idx + 1) % self.capacity
            self.num_items -= 1
            return temp