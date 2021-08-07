"""
Remove Kth Last Element From Linked List  - CodePro (www.techseries.dev)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        n = self
        result = []
        while n:
            result.append(str(n.value))
            n = n.next
        return '->'.join(result)


def remove_k_last(node, k):
    slow_prev = None
    slow = node
    fast = node
    i = 0
    while i < k:
        fast = fast.next
        if not fast:
            return 'IMPOSSIBLE'
        i += 1
    if not fast:
        return node.next

    while fast:
        slow_prev = slow
        slow = slow.next
        fast = fast.next

    slow_prev.next = slow.next

    return node


# 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

print(remove_k_last(head, 3))
# 1->2->3->4->6->7

print(remove_k_last(head, 7))
# 2->3->4->6->7
