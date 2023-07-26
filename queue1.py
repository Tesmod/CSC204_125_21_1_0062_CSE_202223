#FOURTH FILE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


class Queue:
    #Initially, the queue is empty
    def __init__(self):
        self.front = None
        self.rear = None


    def isEmpty(self):
        return self.front == None #If the value of the front element is empty, it will return true which shows the queue is empty
    


    def Enqueue(self, data):
        temp = Node(data)


        if self.rear == None: #The queue is empty
            self.front = temp
            self.rear = temp

        self.rear.next = temp
        self.rear = temp
        
    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data
    
    def sort(self):
        #To sort, the queue is first converted to an ordinary list
        q_list = []
        while not self.isEmpty():
            element = self.dequeue()
            q_list.append(element)
            
        #Sort list
        q_list = sorted(q_list)
        
        #Add the sorted elements back into the queue
        for element in q_list:
            self.Enqueue(element)

    def display(self):
        temp2 = self.front
        while temp2 is not None:
            print(temp2.data)
            temp2 = temp2.next

            
    
#Create an object of the queue class
q = Queue()

#Call the enqueue function and pass the data 1
q.Enqueue(9)
q.Enqueue(8)
q.Enqueue(3)
q.Enqueue(6)
q.Enqueue(1)

q.display()

print("Elements to dequeue are: ")
dq = q.dequeue()
print("Dequeued element: ", dq)

print("Elements to dequeue are: ")
dq = q.dequeue()
print("Dequeued element: ", dq)

print("Elements to dequeue are: ")
dq = q.dequeue()
print("Dequeued element: ", dq)


q.display()
