from linked_list import LinkedList

from linked_list_tail import Linked_list

lst_tail = Linked_list()

lst = LinkedList()
lst.push_front(10)
print(lst.size())
print(lst.pop_front())
print(lst.empty())

lst.push_back(10)
lst.push_back(20)
lst.push_back(30)
lst.push_back(40)



for i in range(lst.size()):

    print(lst.value_at(i))


lst.reverse()

for i in range(lst.size()):

    print(lst.value_at(i))

lst.remove_value(40)


for i in range(lst.size()):

    print(lst.value_at(i))


print()

lst_tail.push_back(10)

for i in range(lst_tail.size()):

    print(lst_tail.value_at(i))