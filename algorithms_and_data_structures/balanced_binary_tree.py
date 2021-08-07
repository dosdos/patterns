"""
Balanced binary tree  - CodePro problem 38 (www.techseries.dev)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _is_balanced_helper(node):
    if not node:
        return True, 0

    is_left_balanced, height_left = _is_balanced_helper(node.left)
    is_right_balanced, height_right = _is_balanced_helper(node.right)

    curr_is_balanced = \
        is_left_balanced and \
        is_right_balanced and \
        abs(height_left - height_right) <= 1
    curr_height = max(height_left, height_right)
    return curr_is_balanced, curr_height + 1


def is_balanced(root_node):
    return _is_balanced_helper(root_node)[0]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(is_balanced(root))
# True

root.left.right = Node(5)
print(is_balanced(root))
# True

root.left.right.right = Node(7)
print(is_balanced(root))
# False

root.left.right.right = None
root.right = None
print(is_balanced(root))
# False
