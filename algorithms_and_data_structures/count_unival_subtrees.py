class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_unival(node):
    if not node.left and not node.right:
        return 1


def count_unival_subtrees(root):

    return is_unival(root)


#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)

print(count_unival_subtrees(root))

