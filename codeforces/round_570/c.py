q = int(input())

for i in range(q):
    k, n, a, b = [int(x) for x in input().split(' ')]
    if k // b == 0:
        print(-1)
    elif k // a >= n:
        print(k // a)
    else:
        total = 0
        while True:
            if n == 0:
                break
            tmp_full = k // a
            if
