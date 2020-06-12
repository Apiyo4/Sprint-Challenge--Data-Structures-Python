class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        
       if not self.head:
           return False 
       #Set previous as None, current as head and next as the next node of current
       previous = None
       current = self.head
       next_node = current.get_next()
  
       #Loop through the linked list until current is None

       #O(n)

       while current:
           #set the next node of current to previous
           current.set_next(previous)     

           # set previous as current, current as next and next as its next node   
           previous = current
           current = next_node
           if next_node:
               next_node = next_node.get_next()

       #set head pointer to the previous node
       self.head = previous
