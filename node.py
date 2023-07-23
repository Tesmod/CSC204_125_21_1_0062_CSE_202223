

class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data #initializes the data and the link to the next node which  are by default None
        self.nextNode = next_node #stores the pointer to the next node
        
    def get_data(self): #returns the data stored on the node
        return self.data
    
    def set_data(self, new_data):#updates the data stored in the node
        self.data = new_data
    
    def get_next(self): #returns the reference to the next node
        return self.next_node
    
    def set_next(self, new_next):#updates the reference to the next node
        self.next_node = new_next
        