n, k = [int(x) for x in input().split(' ')]

questions = [int(x) for x in input().split(' ')]

total = 3 * n - 2
visited_combo = {}
visited = [0] * (n+1)

for i in range(k):
    q = questions[i]
    if not visited[q]:
        visited[q] = 1
        total -= 1
        visited_combo[(q, q)] = True
    # import code
    # code.interact(local=locals())
    if q > 1 and visited[q-1] > 0 and not visited_combo.get((q, q-1), False):
        total -= 1
        visited_combo[(q, q-1)] = True

    if q < n and visited[q+1] > 0 and not visited_combo.get((q, q+1), False):
        total -= 1
        visited_combo[(q, q + 1)] = True

print(total)
