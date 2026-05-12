from queue import Queue

lst = []
q = Queue()
print(q.empty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.empty())

lst.append(q.dequeue())
lst.append(q.dequeue())
lst.append(q.dequeue())

print(q.empty())

print(lst)





