"""
Given a word w and a string s, find all indices in s which are the starting locations of anagrams of w. For example, given w is "ab" and s is "abxaba", return [0, 3, 4]
"""
w = input()
s = input()

len_s = len(s)
len_w = len(w)
res = []

def is_anagram(first, second, n):
    first_array = [0] * 26
    second_array = [0] * 26
    for i in range(n):
        first_array[ord(first[i]) - 97] += 1
        second_array[ord(second[i]) - 97] += 1
    return first_array == second_array

for i in range(len_s - len_w + 1):
    tmp = s[i:i+len_w]
    if is_anagram(w, tmp, len_w):
        res.append(i)

print(res)
