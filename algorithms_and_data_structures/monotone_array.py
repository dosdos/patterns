def longest_monotone(arr):
    """
    :param arr: list of integers
    :return: the starting index of the bibbest monotone sequence in the given arr
    """
    if not arr:
        return -1
    starting_idx = max_idx = 0
    curr_size = max_size = 1
    for idx in range(len(arr)-1):  # from 0 to 5
        if arr[idx+1] > arr[idx]:  # 1 4
            curr_size += 1             # curr_size =
            if curr_size > max_size:
                max_size = curr_size   # max_size = 2
                max_idx = starting_idx   # max_idx = 1
        else:
            starting_idx = idx + 1
            curr_size = 1
    return max_idx


print(longest_monotone([4, 1, 2, 3, 4, 1, 2]))
# print 0
print(longest_monotone([2]))
# print 0
print(longest_monotone([]))
# print 0

