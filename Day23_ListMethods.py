l = [4, 7, 5, 2, 5, 45, 56, 43, 7, 3]
print(l)

l.append(10)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(4))  # it will give take the index value from user and give the index number on which this lies.

print(l.count(5))


m = l
m[0] = 0
print(l)


m = l.copy()
m[0] = 0
print(l)
print(m)


l.insert(1,899)   # it will insert the value as 899 on 1 index number
print(l)


m1 = [100, 200, 300, 400]
l.extend(m1)
print(l)
# l.append(10)
# print(l)  