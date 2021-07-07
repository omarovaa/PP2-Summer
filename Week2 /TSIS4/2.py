import re

flag = False

for i in range(int(input())):
    s = input()
    if '{' in s:
        flag = True
    elif '}' in s:
        flag = False
    elif flag:
        for hexi in re.findall("#[0-9a-fA-F]{3,6}", s):
            print(hexi)