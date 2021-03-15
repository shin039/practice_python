# coding:UTF-8

l1 = ["a", "b", "c", "d"]

print(l1)
print(l1[2])
print(l1[1:3])
print(l1[1:])
print(l1[:3])
print(l1[1:-1])
print(l1[:])

print(len(l1))

l1[1] = "B"
print(l1)

l2 = ["E", "F", "G", "H"]

print(l1+l2)

del(l1[1:3])
print(l1)

print("a"     in l1)
print("B" not in l1)

print(l1.index("a"))

l1.append("e")
print(l1)

l1.insert(1, "b")
l1.insert(2, "c")
print(l1)

l1.remove("e")
print(l1)

l3 = [1, 6, -1, 0, 7]
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)
