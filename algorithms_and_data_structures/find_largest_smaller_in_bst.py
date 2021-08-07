##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.best = None

    def find_largest_smaller_key___(self, num):
        self.best = None
        self.find_largest_smaller_helper(num, self.root)
        return self.best

    def find_largest_smaller_helper(self, num, node):
        print(num, node.key if node else '')
        if node is None:
            return
        if node.key > num:
            self.find_largest_smaller_helper(num, node.left)
        else:
            self.best = node.key
            self.find_largest_smaller_helper(num, node.right)

    def find_largest_smaller_key(self, num):
        # your code goes here
        if self.root == None:
            return -1
        ans = -1

        def traverse(node, num, best):
            if node == None:
                ans = best
                return
            if node.key == num:
                ans = node.key
                return
            elif num < node.key:
                traverse(node.left, num, best)
            else:
                traverse(node.right, num, node.key)

        traverse(self.root, num, ans)
        return ans

        # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):

        # 1) If tree is empty, create the root
        if self.root is None:
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        current_node = self.root
        new_node = Node(key)

        while current_node is not None:
            if key < current_node.key:
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.right


class TestAnonLetter(unittest.TestCase):

    def test_can_be_anonymized(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(9)
        bst.insert(25)
        bst.insert(5)
        bst.insert(12)
        bst.insert(11)
        bst.insert(14)
        self.assertEqual(bst.find_largest_smaller_key(17), 14)
        # self.assertEqual(bst.find_largest_smaller_key(12), 12)
        # self.assertEqual(bst.find_largest_smaller_key(22), 20)
        # self.assertEqual(bst.find_largest_smaller_key(28), 25)
        # self.assertEqual(bst.find_largest_smaller_key(2), None)


if __name__ == '__main__':
    unittest.main()
