n = int(input())
flowers = [int(x) for x in input().split(' ')]

flowers = sorted(flowers)

if flowers[0] == flowers[-1]:
    print("{} {}".format(0, n * (n-1) // 2))
else:
    minimals = 0
    index_start = 0
    while True:
        if flowers[0] == flowers[index_start]:
            minimals += 1
            index_start += 1
        else:
            break

    maximals = 0
    index_end = n-1
    while True:
        if flowers[-1] == flowers[index_end]:
            maximals += 1
            index_end -= 1
        else:
            break
    print("{} {}".format(flowers[-1] - flowers[0], maximals * minimals))

