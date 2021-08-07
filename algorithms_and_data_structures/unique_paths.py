"""
Unique Paths - CodePro (www.techseries.dev)
"""
from time import time


class Solution(object):
    def unique_paths(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.unique_paths(m - 1, n) + self.unique_paths(m, n - 1)

    @staticmethod
    def unique_paths_dp(m, n):
        cache = [[0] * n] * m
        for i in range(m):
            cache[i][0] = 1
        for j in range(n):
            cache[0][j] = 1

        for c in range(1, m):
            for r in range(1, n):
                cache[c][r] = cache[c][r-1] + cache[c-1][r]
        return cache[-1][-1]


start = time()
print(Solution().unique_paths(11, 7))
# 15
print(time()-start)

start = time()
print(Solution().unique_paths_dp(11, 7))
# 15
print(time()-start)
