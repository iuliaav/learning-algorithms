from collections import defaultdict

d = {}
n = int(input())
nums = input().split(' ')
totals = 0
all_items = set()
eliminated = set()

for i in range(n):
    num = int(nums[i])
    if d.get(num, None) is not None:
        cur = d.get(num)
        if cur["failed"]:
            continue
        if cur["distance"] == 0:
            cur["distance"] = i - cur["last"]
            cur["last"] = i
        elif i - cur["last"] != cur["distance"]:
            cur["failed"] = True
            totals -= 1
            eliminated.add(num)

        else:
            cur["last"] = i
    else:
        d[num] = {
            "last": i,
            "distance": 0,
            "failed": False
        }
        all_items.add(num)
        totals += 1

good_items = sorted(all_items - eliminated)
result = [(item, d[item]["distance"]) for item in good_items]

print(totals)
for i, v in enumerate(result):
    print(v[0], v[1])
