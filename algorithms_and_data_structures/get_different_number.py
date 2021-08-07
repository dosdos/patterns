import heapq


def get_different_number(arr):

    heap = []
    for element in arr:
        heapq.heappush(heap, element)
    counter = 0
    while heap:
        heap_value = heapq.heappop(heap)
        print(heap_value, counter)
        if heap_value != counter:
            return counter+1
        else:
            counter += 1

    return counter


print(get_different_number([0, 1, 2, 4, 111]))
