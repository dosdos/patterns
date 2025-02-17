"""
Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four
numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an
ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one
you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:
input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
"""


def check_sum(part, arr):
    head = 0
    tail = len(arr) - 1
    while head < tail:
        if arr[head] + arr[tail] == part:
            return arr[head], arr[tail]
        if arr[head] + arr[tail] > part:
            tail -= 1
        else:
            head += 1
    return []


def find_array_quadruplet(arr, s):
    d = dict()
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            d[arr[i] + arr[j]] = (arr[i], arr[j])

    arr = sorted(arr)
    for k in d.keys():
        tmp = check_sum(s - k, arr)
        # TODO: pop n1 and n2!!
        if tmp:
            return sorted([tmp[0], tmp[1], d[k][0], d[k][1]])
    return []


example = [2, 7, 4, 0, 9, 5, 1, 3]
print(find_array_quadruplet(example, 20))
# print [0, 4, 7, 9]
example = [4, 4, 4, 2]
print(find_array_quadruplet(example, 16))
# print []
