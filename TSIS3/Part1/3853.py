import collections
a = list(map(int, input().split()))
d = collections.deque(a)
k = int(input())
d.rotate(k)
for i in range(len(a)):
    print(d[i], end=' ')