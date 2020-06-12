from doubly_linked_list import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, item):
       #if the buffer's capacity is full
       if self.capacity == len(self.storage):
       #set the new item to the current value
           self.current.value = item
       #Move current to the next depending on the position
       #if it's at the tail
           if self.current == self.storage.tail:
       #then current should move to the head        
               self.current = self.storage.head
        #otherwise
           else:
        #move the current to the next 
               self.current = self.current.next 
       #otherwise
       else:
       #add items to the end of buffer
           self.storage.add_to_tail(item)    
       #if storage has one item
       if len(self.storage) == 1:
       #set the current to the head 
           self.current = self.storage.head     

    def get(self):
        # create a list to hold values
        buffer_list = []
        # define a pointer that points to the storage head
        current_node = self.storage.head
        #Create a loop that loops whenever the current_node is not none
        while current_node:
        #add the value being pointed to the buffer list
            buffer_list.append(current_node.value)
        #move the pointer to the next
            current_node =  current_node.next
        #returns all of the elements in the buffer in a list
        return buffer_list
