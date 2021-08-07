"""
Count Number of Unival Subtrees  - CodePro problem 39 (www.techseries.dev)


is_unival_subtree(node)
    return
        1. left is None or (is_unival_subtree(node.left) and node.val == node.left.val)
        and
        2. right is None or (is_unival_subtree(node.right) and node.val == node.right.val)


"""


class Node:
    def __init__(self, val=False):
        self.val = val
        self.left = None
        self.right = None


#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

root = Node(True)
root.left = Node(True)
root.right = Node(False)
root.right.left = Node(True)
root.right.right = Node(False)
root.right.left.left = Node(True)
root.right.left.right = Node(True)
