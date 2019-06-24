limak, bob = [int(x) for x in input().split(' ')]

count = 0

while True:
    if limak > bob:
        break
    count += 1
    limak *= 3
    bob *= 2

print(count)
