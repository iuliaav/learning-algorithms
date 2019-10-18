a = input()

def increment(n):
    s = sum([int(x) for x in list(str(n))])
    if s % 4 == 0:
        return n
    else:
        return increment(n + (4 - s % 4))

print(increment(int(a)))
