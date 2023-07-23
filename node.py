#TASK 1
    #Create a Node class in package nodes which stores data and link to another node
    #Then create a Singly Linked List class in package linkedlist
    #Test with the list [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28] by performing create, insertion and display methods and then other list operations
    #Test run the code using a main.py file

#TASK 2
    #Implement the method to find the minimum and maximum data in the singly linked list. Classes used for task 1 can be used
    #Implement the method that converts the single linked list into a binary search tree
    #The method takes the list [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28] as argument

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
        