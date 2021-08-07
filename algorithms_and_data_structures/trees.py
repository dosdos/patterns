import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        # If tree is empty, create the root
        if not self.root:
            self.root = Node(value)
            return

        current_node = self.root
        new_node = Node(value)

        # Otherwise, create a node with the key and traverse down the tree to find where to to insert the new node
        while current_node:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.right

    def find_largest_smaller_value(self, num):
        def helper(n, node, best):
            if node is None:
                return best
            if node.value > n:
                return helper(n, node.left, best)
            else:
                return helper(n, node.right, node.value)
        return helper(num, self.root, None)

    @staticmethod
    def is_valid_BST(tree):
        pass


class TestBinarySearchTree(unittest.TestCase):

    def test_find_largest_smaller_value(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(9)
        bst.insert(25)
        bst.insert(5)
        bst.insert(12)
        bst.insert(11)
        bst.insert(14)
        self.assertEqual(bst.find_largest_smaller_value(17), 14)
        self.assertEqual(bst.find_largest_smaller_value(12), 12)
        self.assertEqual(bst.find_largest_smaller_value(22), 20)
        self.assertEqual(bst.find_largest_smaller_value(28), 25)
        self.assertEqual(bst.find_largest_smaller_value(2), None)

    def test_is_bst(self):
        root = Node(12)
        root.left = Node(9)
        root.right = Node(20)
        self.assertTrue(BinarySearchTree.is_valid_BST(root))
        root.left.left = Node(5)
        root.left.right = Node(11)
        root.right.left = Node(10)
        root.right.right = Node(25)


if __name__ == '__main__':
    unittest.main()
