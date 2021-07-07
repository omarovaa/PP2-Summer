n, m = input().split()
a, b = set(), set()
for i in range(int(n)):
    a.add(int(input()))
for i in range(int(m)):
    b.add(int(input()))
print(len(a & b))
print(*sorted(a & b, key=int))
print(len(a - b))
print(*sorted(a - b, key=int))
print(len(b - a))
print(*sorted(b - a, key=int))