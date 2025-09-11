class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            # If the list is empty, new node becomes the head
            self.head = new_node
            return
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        # Update the last node's next pointer to the new node
        current.next = new_node
    def delete_value(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    # Bypass the current node by updating previous node's next pointer
                    prev.next = current.next
                else:
                    # If deleting the head, move head pointer to next node
                    self.head = current.next
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next  # Move to the next node
        return elements
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
print("After insertions:", ll.traverse())  
ll.delete_value(10)
print("After deleting head (10):", ll.traverse()) 
ll.insert_at_end(40)
ll.delete_value(30)
print("After deleting middle (30):", ll.traverse())  
ll.delete_value(40)
print("After deleting last (40):", ll.traverse())  
result = ll.delete_value(100)
print("Delete non-existent (100):", result, ll.traverse())  
ll.delete_value(20)
print("After deleting only element (20):", ll.traverse())  
ll.insert_at_end(50)
print("After inserting into empty list:", ll.traverse())  