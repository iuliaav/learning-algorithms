from math import gcd
from collections import defaultdict
n = int(input())

coord = [[int(x) for x in input().split()] for i in range(n)]
wires = set()

for i in range(n-1):
    for j in range(i+1, n):
        a = coord[i][1] - coord[j][1]
        b = coord[i][0] - coord[j][0]
        c = coord[i][1]*coord[j][0] - coord[j][1]*coord[i][0]

        divisor = gcd(gcd(a, b), c)

        wires.add((a//divisor, b//divisor, c//divisor))


slopes = defaultdict(int)
wires_num = len(wires)
total = wires_num * (wires_num-1) // 2

for wire in wires:
    slope = (wire[0], wire[1])
    slopes[slope] += 1

for key, value in slopes.items():
    if value > 1:
        total -= value*(value-1)//2

print(total)