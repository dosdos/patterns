"""
Get all Values at a Certain Height in a Binary Tree  - CodePro problem 37 (www.techseries.dev)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def get_nodes_at_level(current_node, level):
    """
    :param current_node: Node instance
    :param level: int num
    :return: list of int (the node values)
    """
    if not current_node:
        return []
    if level == 1:
        return [current_node.value]
    return get_nodes_at_level(current_node.left, level - 1) + get_nodes_at_level(current_node.right, level - 1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

print(get_nodes_at_level(root, 1))
# [1]

print(get_nodes_at_level(root, 2))
# [2, 3]

print(get_nodes_at_level(root, 3))
# [4, 5, 7]

print(get_nodes_at_level(root, 4))
# []
