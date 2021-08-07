"""
Array of Array Products  -  Pramp.com
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the
integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers
and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.
"""


def array_of_array_products_slow(arr):
    """
    in = [2, 3, 4, 5]
    out = [3*4*5, 2*4*5, 3*4*5, 2*3*4]

    [2, 3, 4, 5]

    prev = [1, 2, 2*3, 2*3*4]
    post = [3*4*5, 4*5, 5, 1]

    result for index i = prev[i-1] * post[i+1]

    """
    result = []
    if len(arr) <= 1:
        return result

    for idx, x in enumerate(arr):
        mult = 1
        for jdx, y in enumerate(arr):
            if idx != jdx:
                mult *= arr[jdx]
        result.append(mult)
    return result


def array_of_array_products(arr):
    """
    prev = [1, 2, 2*3, 2*3*4]
    post = [3*4*5, 4*5, 5, 1]

    result for index i = prev[i-1] * post[i+1]
    """
    arr_len = len(arr)
    result = []
    if arr_len <= 1:
        return result

    product = 1
    for i in range(arr_len):
        result.append(product)
        product *= arr[i]

    product = 1
    for i in range(arr_len - 1, -1, -1):
        result[i] *= product
        product *= arr[i]
    return result


print(array_of_array_products([2,2]))
print(array_of_array_products_slow([2,2]))

print(array_of_array_products([8, 10, 2]))
print(array_of_array_products_slow([8, 10, 2]))

print(array_of_array_products([2, 7, 3, 4]))
print(array_of_array_products_slow([2, 7, 3, 4]))
