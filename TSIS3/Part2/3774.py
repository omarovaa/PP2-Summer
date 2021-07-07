n = int(input())
d = {}
a = {}
for i in range(n-1):
    char, par = input().split()
    d[par] = char
    a[char] = 0
    a[par] = 0
for i in d:
    s = i
    while s in d:
        s = d[s]
        a[i] += 1
for i in sorted(a):
    print(i, a[i])