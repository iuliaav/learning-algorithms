"""
One day shooshuns found a sequence of n integers, written on a blackboard.
The shooshuns can perform one operation with it, the operation consists of two steps:

1. Find the number that goes k-th in the current sequence and add the same number to the end of the sequence;
2. Delete the first number of the current sequence.

The shooshuns wonder after how many operations all numbers on the board will be the same and
whether all numbers will ever be the same.

Input
The first line contains two space-separated integers n and k (1 ≤ k ≤ n ≤ 105).

The second line contains n space-separated integers: a1, a2, ..., an (1 ≤ ai ≤ 105)
 — the sequence that the shooshuns found.

Output
Print the minimum number of operations, required for all numbers on the blackboard to become the same.
If it is impossible to achieve, print -1.

Example:
    - input
3 2
3 1 1
    - output
1

3 1 1 -> 3 1 1 1 -> 1 1 1

    - input
3 1
3 1 1
    - output
-1
3 1 1 -> 3 1 1 3 -> 1 1 3 -> 1 1 3 1 -> 1 3 1 -> 1 3 1 1 -> 3 1 1
"""


n, k = [int(x) for x in input().split(' ')]
A = input().split(' ')

to_compare = A[k-1]
possible = True
for i in range(k-1, n):
    if A[i] != to_compare:
        possible = False
        break

if not possible:
    print(-1)
else:
    result = 0
    for i in range(k-2, -1, -1):
        if A[i] != to_compare:
            result = i + 1
            break
    print(result)
