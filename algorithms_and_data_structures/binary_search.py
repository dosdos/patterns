def binary_search(arr, elem):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # print(left, mid, right)
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            right = mid - 1
        elif arr[mid] < elem:
            left = mid + 1
    return -1


print(binary_search(list(range(30)), 31))
# -1
print(binary_search([0, 2, 3, 4, 6, 8], 2))
# 1
print(binary_search([0, 2, 3, 4, 6, 8], 0))
# 0
print(binary_search([0, 2, 3, 4, 6, 8], 8))
# 5
print(binary_search([0, 2, 3, 4, 6, 8], 11))
# -1
print(binary_search([0, 2, 3, 4, 6, 8], 1))
# -1
print(binary_search([0, 2, 3, 4, 6, 8], 5))
# -1
print(binary_search([0, 2, 3, 4, 6, 8, 21, 22, 23], 20))
# -1
