class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next})"


def swap_every_two(ll):
    head = ll

    curr = head
    while curr is not None and curr.next is not None:
        curr.value, curr.next.value = curr.next.value, curr.value
        curr = curr.next.next

    return head


llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))  # 2, (1, (4, (3, (5, (None)))))
