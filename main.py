from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def join_node(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print("None")
        

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count
    

    def reverse(self):
        prev =  None
        current = self.head
        while current:
            next_node = current.get_next()
            current.set_next(prev)
            prev = current
            current = next_node
        self.head = prev

    
    def create_from_list(self, input_list):
        for data in input_list:
            self.join_node(data)


input_list = [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]

linked_list = SinglyLinkedList()
linked_list.create_from_list(input_list)


print("The Linked List is given  as:")
linked_list.display()

linked_list.reverse()

print("The reversed Linked List is given as:")
linked_list.display()

print("The Length of the node is: ", linked_list.length())

