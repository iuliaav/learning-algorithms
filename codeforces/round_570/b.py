q = int(input())
#result = []
for i in range(q):
    n, k = [int(x) for x in input().split(' ')]
    a = [int(x) for x in input().split(' ')]
    l1 = min(a)
    l2 = max(a)
    if l2 - l1 > 2*k:
        print(-1)
    else:
        print(l1 + k)

#print("\n".join([str(x) for x in result]))
