from vector import Vector

v = Vector()

v.push(10)
v.push(20)
v.push(30)
v.push(40)
v.push(50)
v.push(60)

for i in range(1,21):
    v.push(i)

print(v.size())       # 6
print(v.capacity())   # 16
print(v.is_empty())   # False


print(v.capacity())


print(v.data)
v.remove(20)
print(v.data)

print(v.find(3))




