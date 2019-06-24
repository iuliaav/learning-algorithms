from collections import defaultdict
n = int(input())

colors = [int(x) for x in input().split(' ')]

colors_visited = [0] * ((10 ** 5) + 5)
occurence_counter = [0] * ((10 ** 5) + 5)
mx = 0
ans = 0

for i in range(1, n+1):
    color = colors[i-1]
    occurence_counter[colors_visited[color]] -= 1
    colors_visited[color] += 1
    occurence_counter[colors_visited[color]] += 1

    mx = max(mx, colors_visited[color])
    ok = False

    if occurence_counter[1] == i:
        ok = True
    elif occurence_counter[i] == 1:
        ok = True
    elif occurence_counter[1] == 1 and occurence_counter[mx] * mx == i - 1:
        ok = True
    elif occurence_counter[mx - 1] * (mx - 1) == i - mx and occurence_counter[mx] == 1:
        ok = True
    if ok:
        ans = i


print(ans)


