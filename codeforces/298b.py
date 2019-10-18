from math import sqrt

t, sx, sy, ex, ey = [int(x) for x in input().split(' ')]
wind = list(input())
arrive_time = -1
found = False

for i in range(t):
    prev = (sx, sy)
    prev_distance = sqrt((ex - sx) ** 2 + (ey - sy) ** 2)
    if wind[i] == "S":
        sy -= 1
    elif wind[i] == "E":
        sx += 1
    elif wind[i] == "W":
        sx -= 1
    else:
        sy += 1

    new_distance = sqrt((ex - sx) ** 2 + (ey - sy) ** 2)
    if prev_distance < new_distance:
        sx = prev[0]
        sy = prev[1]

    if sx == ex and sy == ey:
        arrive_time = i
        found = True
        break

if found:
    print(arrive_time + 1)
else:
    print(-1)