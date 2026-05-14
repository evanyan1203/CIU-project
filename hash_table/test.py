from implement import HashTable

ht = HashTable()

ht.add(0,1)
ht.add(1,2)
ht.add(2,3)
ht.add(3,40)

for i in ht.table:
    print(i)

print(ht.exists(0))

ht.remove(0)

for i in ht.table:
    print(i)

print()