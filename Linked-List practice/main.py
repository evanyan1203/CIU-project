from linked_list import LinkedList

lst = LinkedList()
lst.push_front(10)
print(lst.size())
print(lst.pop_front())
print(lst.empty())
lst.push_back(20)
lst.push_back(30)

print(lst.value_at(1))



