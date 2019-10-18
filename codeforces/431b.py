from itertools import permutations

lines = []
for i in range(5):
    lines.append([int(x) for x in input().split(" ")])

max_thus_far = 0
pairs = []
perm = permutations([0, 1, 2, 3, 4])
for i in list(perm):
    s = (
        lines[i[0]][i[1]]
        + lines[i[1]][i[0]]
        + 2 * (lines[i[2]][i[3]] + lines[i[3]][i[2]])
        + lines[i[1]][i[2]]
        + lines[i[2]][i[1]]
        + 2 * (lines[i[4]][i[3]] + lines[i[3]][i[4]])
    )

    if s > max_thus_far:
        max_thus_far = s

print(max_thus_far)
