n = int(input())
numbers = [int(x) for x in input().split(" ")]
possibilities = {
    1: numbers.count(1),
    2: numbers.count(2),
    3: numbers.count(3),
    4: numbers.count(4),
    6: numbers.count(6),
}

if (
    possibilities[1] == n // 3
    and possibilities[2] + possibilities[3] == n // 3
    and possibilities[4] + possibilities[6] == n // 3
    and possibilities[4] <= possibilities[2]
    and possibilities[6] >= possibilities[3]
):
    for i in range(possibilities[3]):
        print(1, 3, 6)
    for i in range(possibilities[4]):
        print(1, 2, 4)
    for i in range(possibilities[6] - possibilities[3]):
        print(1, 2, 6)
else:
    print(-1)
