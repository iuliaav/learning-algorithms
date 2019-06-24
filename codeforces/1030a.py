n = int(input())
problems = [int(x) for x in input().split(' ')]

if sum(problems) > 0:
    print("hard")
else:
    print("easy")

