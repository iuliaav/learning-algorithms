"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

Follow-up: without division
"""
from functools import reduce
from operator import mul

class Solution:
    def obvious(self, array):
        product = reduce(mul, array, 1)
        return [product // x for x in array]

    def without_division(self):
        pass

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 6]

    solution = Solution()
    print(solution.obvious(a))
