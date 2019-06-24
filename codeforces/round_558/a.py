n, m = [int(x) for x in input().split(' ')]

if m == n:
    print(0)
elif m == 0:
    print(1)
else:
    middle = [n // 2]
    if n % 2 == 1:
        middle.append(middle[0] + 1)
    if m not in middle:
        if m > middle[-1]:
            print(middle[0] - abs(m-middle[-1]))
        else:
            print(m)
    else:
        print(middle[0])