import unittest
from Lab4_2 import CircularLinkedList
class TestCircularLinkedList(unittest.TestCase):
    def setUp(self):
        self.circular_list = CircularLinkedList()
    
    def test_append(self):
        self.circular_list.append(5)
        self.circular_list.append(7)
        self.circular_list.append(2)
        self.circular_list.append(-3)
        self.assertEqual(self.circular_list.head.data, 5)
        self.assertEqual(self.circular_list.head.next.data, 7)
        self.assertEqual(self.circular_list.head.next.next.data, 2)
        self.assertEqual(self.circular_list.head.next.next.next.data, -3)
        self.assertEqual(self.circular_list.head.next.next.next.next, self.circular_list.head)
        
    def test_print_list(self):
        self.circular_list.append(5)
        self.circular_list.append(7)
        self.circular_list.append(2)
        self.circular_list.append(-3)
        self.assertEqual(self.circular_list.print_list(), print("5\n7\n2\n-3"))
        
    def test_sum_positive(self):
        self.circular_list.append(5)
        self.circular_list.append(-3)
        self.circular_list.append(10)
        self.circular_list.append(-7)
        self.assertEqual(self.circular_list.sum_positive(), 15)
        
    def test_sum_positive_empty_list(self):
        self.assertEqual(self.circular_list.sum_positive(), 0)
        
if __name__ == '__main__':
    unittest.main()
