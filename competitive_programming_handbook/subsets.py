n = int(input())
subset = []

def search(k):
    if k == n:
        pass
    else:
        search(k+1)
        subset.append(k)
        search(k+1)
        subset.pop(-1)


search(0)
print(subset)
