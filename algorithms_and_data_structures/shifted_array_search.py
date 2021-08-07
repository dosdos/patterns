"""
Shifted Array Search (Pramp.com)
A sorted array of distinct integers  is shifted to the left by an unknown offset and you don't have a pre-shifted copy
of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.
Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num
in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

Time Complexity: the time complexity of findPivotPoint is O(log((N)) since it’s essentially a slightly modified
version of the binary search algorithm. The time complexity of binarySearch is obviously O(log((N)) as well.
The total time complexity is therefore O(log((N)).

Space Complexity: throughout the entire algorithm we used only a constant amount of space, hence
the space complexity is O(1).
"""


def shifted_arr_search(shiftArr, num):
    shift = 0
    for i in range(len(shiftArr)):
        if i >= len(shiftArr) - 1 or shiftArr[i] > shiftArr[i + 1]:
            break
        shift += 1

    j = len(shiftArr) // 2 - shift
    if j < 0:
        j = len(shiftArr) + j

    while shiftArr[j] != num:
        if shiftArr[j] > num:
            j = j + (j // 2) - shift
        else:
            j = j - (j // 2) - shift
        if j < 0:
            j = len(shiftArr) + j

    return j


'''
num is target num=1
[3,4,5,1,2]
3
4
5

'''

arr = [1, 5]
print(shifted_arr_search(arr, 1))  # 0

arr = [1, 2]
print(shifted_arr_search(arr, 2))  # 1

arr = [3, 4, 5, 1, 2]
print(shifted_arr_search(arr, 2))  # 4

arr = [6, 9, 12, 17, 2, 4, 5]
print(shifted_arr_search(arr, 4))  # 5
