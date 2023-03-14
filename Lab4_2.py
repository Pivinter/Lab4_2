class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            self._append_helper(self.head, new_node)
            
    def _append_helper(self, current, new_node):
        if current.next == self.head:
            current.next = new_node
            new_node.next = self.head
        else:
            self._append_helper(current.next, new_node)
    
    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            self._print_helper(self.head)
    
    def _print_helper(self, current):
        print(current.data)
        if current.next != self.head:
            self._print_helper(current.next)
    
    def sum_positive(self):
        if self.head is None:
            return 0
        else:
            return self._sum_positive_helper(self.head, 0)
        
    def _sum_positive_helper(self, current, sum):
        if current.data > 0:
            sum += current.data
        if current.next == self.head:
            return sum
        else:
            return self._sum_positive_helper(current.next, sum)
        
circular_list = CircularLinkedList() #1
circular_list.append(5) #2
circular_list.append(-3) #3
circular_list.append(10) #4
circular_list.append(-7) #5
circular_list.print_list()
print("Sum:")
print(circular_list.sum_positive())
