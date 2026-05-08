# Implement using linked-list, with tail pointer:

# enqueue(value) - adds value at a position at the tail
# dequeue() - returns value and removes least recently added element (front)
# empty()
#  Implement using a fixed-sized array:
# enqueue(value) - adds item at end of available storage
# dequeue() - returns value and removes least recently added element
# empty()
# full()
#  Cost:
# a bad implementation using a linked list where you enqueue at the head and dequeue at the tail would be O(n) because you'd need the next to last element, causing a full traversal of each dequeue
# enqueue: O(1) (amortized, linked list and array [probing])
# dequeue: O(1) (linked list and array)
# empty: O(1) (linked list and array)