from linked_list import LinkedList

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

