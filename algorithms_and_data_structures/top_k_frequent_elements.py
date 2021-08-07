import collections
import heapq


def top_k_frequent_old(arr, k):
    counter = collections.defaultdict(int)
    for e in arr:
        counter[e] += 1
    heap = []
    for e, c in counter.items():
        heap.append((-c, e))
    heapq.heapify(heap)

    result = []
    for i in range(k):
        result.append(heapq.heappop(heap)[1])

    return result


def top_k_frequent(arr, k):
    counters = collections.defaultdict(int)
    for e in arr:
        counters[e] += 1
    heap = []
    heapq.heapify(heap)
    for e, c in counters.items():
        heapq.heappush(heap, (-c, e))
    result = []
    while heap and len(result) < k:
        result.append(heapq.heappop(heap)[1])
    return result


print(top_k_frequent([1, 1, 1, 2, 2, 3, 1], 2))
# [1, 2]
print(top_k_frequent([1, 1, 1, 2, 2, 3, 1], 1))
# [1]
print(top_k_frequent([1, 1, 3, 3, 3, 1, 2, 2, 3, 1], 2))
# [1, 3]
print(top_k_frequent([1, 1, 3, 3, 3, 1, 2, 2, 3, 1], 5))
# [1, 3, 2]
