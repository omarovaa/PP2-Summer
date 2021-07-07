l = list(map(int, input().split()))
l.sort(key=lambda x: not x)
for i in range(len(l)):
    print(l[i], end=" ")