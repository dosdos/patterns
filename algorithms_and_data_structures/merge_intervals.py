"""
Merge Intervals  - CodePro problem 52 (www.techseries.dev)
"""


def merge_intervals(intervals):
    """
    requisite: all given (x, y) intervals are valid -> x < y

    :param intervals: tuple of couples of inters; e.g. ([1, 3], [5, 8], [4, 10], [20, 25])
    :return: tuple of couples of inters
    """
    # sort elements by first value
    intervals = sorted(intervals)  # [1, 3], [4, 10], [5, 8], [20, 25]

    # create a list to save merged intervals
    merged_intervals = []

    # save 2 pointers: left and right
    last_interval = intervals[0]  # [1, 3]

    # iterate on sorted elements
    for interval in intervals[1:]:  # [4, 10], [5, 8], [20, 25]
        # if right is greater than the first value of next element
        if last_interval[1] >= interval[0]:
            last_interval = merge(last_interval, interval)
        else:
            merged_intervals.append(list(last_interval))
            last_interval = interval

    return merged_intervals + [last_interval]


def merge(couple_1, couple_2):  # [4, 10], [5, 8]
    return min(couple_1[0], couple_2[0]), max(couple_1[1], couple_2[1])  # [4, 10]


print(merge_intervals(([1, 3], [5, 8], [4, 10], [20, 25])))
# [1, 3], [4, 10], [20, 25]
print(merge_intervals(([1, 3], [5, 8], [4, 6], [20, 25])))
# [1, 3], [4, 8], [20, 25]
