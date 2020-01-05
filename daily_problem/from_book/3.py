"""
Given an array of numbers, find the maximum sum of any subcontiguous subarray of the array. Example: [34, -50, 42, 14, -5, 86] => 137
Given the array [-5, -1, -8, -9] the result would be 0 since we would choose not to use any elements.

Solve this in O(n)

sum from left: [34, -16, 26, 40, 35, 121]
sum from right: [121, 87, 137, 95, 81, 86]

"""

def solution(nums):
    m = current = 0
    for num in nums:
        current = max(current + num, 0)
        m = max(m, current)
    return m

print(solution([34, -50, 42, 14, -5, 86]))
print(solution([-5, -1, -8, -9]))
