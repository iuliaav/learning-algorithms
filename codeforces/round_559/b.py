n = int(input())
a = [int(x) for x in input().split(' ')]

tmp = 10 ** 9

sorted = [i[0] for i in sorted(enumerate(a), key=lambda x:x[1])]
for i in range(n-1):
    el_pos = sorted[i]
    el = a[el_pos]
    k = el // max(max(sorted[i+1:]) - el_pos, el_pos - min(sorted[i+1:]))
    if k < tmp:
        tmp = k

print(tmp)