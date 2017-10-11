# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 3
# Term:        Fall 2017

import unittest
import queues

class TestLab3(unittest.TestCase):


    def test_is_empty_1(self):
        # Creates an empty queue and makes sure the function returns true
        queue = queues.QueueLinked(10)
        self.assertTrue(queue.is_empty())

    def test_is_empty_2(self):
        # Creates a queue and then adds an item, makes sure it isn't empty
        queue = queues.QueueLinked(10)
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())


    def test_is_full_1(self):
        # Creates a queue and fills it, makes sure its full
        queue = queues.QueueLinked(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertTrue(queue.is_full())

    def test_is_full_2(self):
        # Creates an queue and makes sure it isn't full
        queue = queues.QueueLinked(10)
        self.assertFalse(queue.is_full())


    def test_num_in_queue_1(self):
        # Creates a queue and adds 4 things, makes sure size is four
        queue = queues.QueueLinked(5)
        for i in range(4):
            queue.enqueue(i)
        self.assertEqual(queue.num_in_queue(), 4)


    def test_enqueue_1(self):
        # Creates a queue, adds one thing, checks size, adds another, checks again
        queue = queues.QueueLinked(10)
        queue.enqueue(1)
        self.assertEqual(queue.num_in_queue(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.num_in_queue(), 2)

    def test_enqueue_2(self):
        # Creates a queue and fills it, makes sure that the next enqueue raises an error
        queue = queues.QueueLinked(10)
        for i in range(10):
            queue.enqueue(i)
        with self.assertRaises(IndexError):
            queue.enqueue(1)


    def test_dequeue_1(self):
        # Creates a queue, adds two things, makes sure they are removed correctly 
        queue = queues.QueueLinked(10)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

    def test_dequeue_2(self):
        # Tries to remove from an empty queue, makes sure an error is raised
        queue = queues.QueueLinked(10)
        with self.assertRaises(IndexError):
            queue.dequeue()


    # The above tests are identical to the next tests except they check a different implementation


    def test_array_is_empty_1(self):
        # Creates an empty queue and makes sure the function returns true
        queue = queues.QueueArray(10)
        self.assertTrue(queue.is_empty())

    def test_array_is_empty_2(self):
        # Creates a queue and then adds an item, makes sure it isn't empty
        queue = queues.QueueArray(10)
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())


    def test_array_is_full_1(self):
        # Creates a queue and fills it, makes sure its full
        queue = queues.QueueArray(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertTrue(queue.is_full())

    def test_array_is_full_2(self):
        # Creates an queue and makes sure it isn't full
        queue = queues.QueueArray(10)
        self.assertFalse(queue.is_full())


    def test_array_num_in_queue_1(self):
        # Creates a queue and adds 4 things, makes sure size is four
        queue = queues.QueueArray(5)
        for i in range(4):
            queue.enqueue(i)
        self.assertEqual(queue.num_in_queue(), 4)


    def test_array_enqueue_1(self):
        # Creates a queue, adds one thing, checks size, adds another, checks again
        queue = queues.QueueArray(10)
        queue.enqueue(1)
        self.assertEqual(queue.num_in_queue(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.num_in_queue(), 2)

    def test_array_enqueue_2(self):
        # Creates a queue and fills it, makes sure that the next enqueue raises an error
        queue = queues.QueueArray(10)
        for i in range(10):
            queue.enqueue(i)
        with self.assertRaises(IndexError):
            queue.enqueue(1)


    def test_array_dequeue_1(self):
        # Creates a queue, adds two things, makes sure they are removed correctly 
        queue = queues.QueueArray(10)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

    def test_array_dequeue_2(self):
        # Tries to remove from an empty queue, makes sure an error is raised
        queue = queues.QueueArray(10)
        with self.assertRaises(IndexError):
            queue.dequeue()


if __name__ == "__main__":
        unittest.main()
