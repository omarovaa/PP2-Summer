n = int(input())
dictor = {}
i = 0
while i < n:
    a, b = input().strip().split()
    dictor[b] = a
    dictor[a] = b
    i += 1
syn = input()
print(dictor[syn])