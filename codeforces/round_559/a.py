n = int(input())
symbols = input()
totals = 0
for character in symbols:
    if character == '-':
        totals = max(0, totals - 1)
    if character == '+':
        totals += 1

print(totals)