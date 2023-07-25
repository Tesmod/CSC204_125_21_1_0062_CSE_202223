from queue import Queue

q = Queue()
q.Enqueue(9)
q.Enqueue(8)
q.Enqueue(3)
q.Enqueue(6)
q.Enqueue(1)

print("The data in the queue before sorting are: ")
q.display()

q.sort() 
print("The sorted queue is then: ")
q.display()