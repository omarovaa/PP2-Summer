from collections import Counter
import sys

lets = str(sys.stdin.read()).split()

c = Counter(sorted(lets))
print(*sorted(c.keys(), key=c.get, reverse=True), sep='\n')