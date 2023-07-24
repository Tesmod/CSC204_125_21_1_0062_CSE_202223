class Nodes:
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
        temp = Nodes(data)


        if self.rear == None: #The queue is empty
            self.front = temp
            self.rear = temp

        self.rear.next = temp
        self.rear = temp

    def display(self):
        temp2 = self.front
        while temp2 is not None:
            print(temp2.data)
            temp2 = temp2.next

#Create an object of the queue class
q = Queue()

#Call the enqueue function and pass the data 1
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)

q.display()