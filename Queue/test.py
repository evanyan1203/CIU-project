# from queue1 import Queue as Queue1

# lst = []
# q = Queue1()
# print(q.empty())
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.empty())

# lst.append(q.dequeue())
# lst.append(q.dequeue())
# lst.append(q.dequeue())

# print(q.empty())

# print(lst)


from queue2 import Queue as Queue2

lst = []
q = Queue2()
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
