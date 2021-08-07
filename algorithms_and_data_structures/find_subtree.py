"""
Find Subtree  - CodePro problem 69 (www.techseries.dev)
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder_traversal(node):
    """Tree Preorder traversal"""
    if not node:
        return '#'
    return '-'.join([str(node.value), preorder_traversal(node.left), preorder_traversal(node.right)])


def postorder_traversal(node):
    """Tree Postorder traversal"""
    if not node:
        return '#'
    return '-'.join([str(node.value), postorder_traversal(node.right), postorder_traversal(node.left)])


def find_subtree(tree_a, tree_b):
    print('PRE: ', preorder_traversal(tree_a))
    print('POST:', postorder_traversal(tree_a))
    print('PRE: ', preorder_traversal(tree_b))
    print('POST:', postorder_traversal(tree_b))
    return preorder_traversal(tree_b) in preorder_traversal(tree_a)


def find_subtree2(a, b):
    if not a:
        return False

    if \
            (a.value == b.value) \
            and ((not a.left or not b.left) or find_subtree2(a.left, b.left)) \
            and ((not a.right or not b.right) or find_subtree2(a.right, b.right)):
        return True

    return find_subtree2(a.left, b) or find_subtree2(a.right, b)


n = Node(1)
n.left = Node(4)
n.right = Node(5)
n.left.left = Node(3)
n.left.right = Node(2)
n.left.right.left = Node(2)
n.right.left = Node(4)
n.right.right = Node(1)

b = Node(4)
b.left = Node(3)
b.right = Node(2)


print(find_subtree(n, b))
# True

print(find_subtree2(n, b))
# True
