def solution(nums):
    l = r = None
    n = len(nums)

    maximum = float('-inf')
    minimum = float('inf')

    for i in range(n):
        left = i
        right = n - i - 1

        maximum = max(maximum, nums[left])
        minimum = min(minimum, nums[right])

        if nums[left] < maximum:
            r = left
        if nums[right] > minimum:
            l = right

    print(l, r)

solution([3, 7, 5, 6, 9])
