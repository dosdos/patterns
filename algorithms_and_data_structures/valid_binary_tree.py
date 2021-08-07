# Check if given tree is a valid Binary Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def helper(node, low, high):
    if not node:
        return True
    if low < node.value < high and helper(node.left, low, node.value) and helper(node.right, node.value, high):
        return True
    return False


def is_valid(tree):
    return helper(tree, float('-inf'), float('inf'))


root = Node(5)
root.left = Node(4)
root.right = Node(7)
root.right.left = Node(2)

print(is_valid(root))
# False

root = Node(5)
root.left = Node(4)
root.right = Node(7)
root.right.left = Node(6)

print(is_valid(root))
# True

root = Node(5)
root.left = Node(4)
root.right = Node(7)
root.right.left = Node(5)
root.right.right = Node(9)
root.right.right.left = Node(3)

print(is_valid(root))
# False
