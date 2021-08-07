def fibonacci_recursive(n):
    """
    :param n: integer greater than or equal to zero
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci(n):  # 3
    prevprev = 0
    prev = 1
    result = 0
    if n == 0:
        return prevprev
    if n == 1:
        return prev

    for i in range(1, n):
        result = prev + prevprev  # 3
        prevprev = prev  # 2
        prev = result  # 3
    return result


print(fibonacci(0))
# 0
print(fibonacci(1))
# 1
print(fibonacci(2))
# 1
print(fibonacci(3))
# 2
print(fibonacci(4))
# 3
print(fibonacci(5))
# 5
print(fibonacci(6))
# 8
