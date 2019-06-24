n = int(input())
array = [int(x) for x in input().split(' ')]
max_negative = [array[0], 0]

for i in range(n):
    if array[i] >= 0:
        array[i] = (-1) * array[i] - 1

    if array[i] < max_negative[0]:
        max_negative[0] = array[i]
        max_negative[1] = i

if n % 2 == 1:
    array[max_negative[1]] = (-1) * max_negative[0] - 1

print(" ".join([str(x) for x in array]))

