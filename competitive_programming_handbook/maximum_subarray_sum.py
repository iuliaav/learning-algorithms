def version_one(array, n):
    # O(n^3)
    best = 0
    for i in range(n):
        for j in range(i, n):
            s = 0
            for k in range(i, j+1):
                s += array[k]
            best = max(best, s)
            print("sum={} for array between {} and {}".format(s, array[i], array[j]))
    return best


def version_two(array, n):
    # O(n^2)
    best = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += array[j]
            best = max(best, s)
            print("sum={} for array between {} and {}".format(s, i, j))
    return best

def version_three(array, n):
    # O(n)
    best = 0
    s = 0
    for i in range(n):
        s = max(array[i], s+array[i])
        best = max(best, s)
        print("at i={}, s={}".format(i, s))

    return best

array = [-1, 2, 4, -3, 5, 2, -5, 2]
#print(version_one(array, len(array)))
#print(version_two(array, len(array)))
print(version_three(array, len(array)))
