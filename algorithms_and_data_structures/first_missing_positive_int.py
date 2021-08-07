"""
First Missing Positive Integer  - CodePro problem 33 (www.techseries.dev)
"""


def find_first_missing_positive_int(arr):
    found = {i for i in arr if i > 0}
    i = 1
    while i in found:
        i += 1
    return i


print(find_first_missing_positive_int([3, 4, -1, 1]))
# 2
print(find_first_missing_positive_int([3, 4, 1, 2]))
# 5
print(find_first_missing_positive_int([0]))
# 1
print(find_first_missing_positive_int([1]))
# 2
print(find_first_missing_positive_int([3]))
# 1
