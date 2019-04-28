"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
Upgraded: do it in one pass
"""

class Solution:
    def obvious_solution(self, numbers, k):
        from collections import defaultdict
        d = defaultdict(int)
	for num in numbers:
            if d[k-num] == 1:
                return True
            d[num] = 1
        return False

if __name__ == "__main__":
    numbers = [10, 15, 3, 7]
    k = 17
    print("Yes" if Solution().obvious_solution(numbers, k) else "No")

