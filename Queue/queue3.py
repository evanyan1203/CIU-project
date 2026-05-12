

#  Cost:
# a bad implementation using a linked list where you enqueue at the head and dequeue at the tail would be O(n) because you'd need the next to last element, causing a full traversal of each dequeue
# enqueue: O(1) (amortized, linked list and array [probing])
# dequeue: O(1) (linked list and array)
# empty: O(1) (linked list and array)