class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, left=node4, right=node5)
node3 = TreeNode(3)
root = TreeNode(1, left=node2, right=node3)


node4_mirror = TreeNode(4)
node5_mirror = TreeNode(5)
node2_mirror = TreeNode(2, left=node5_mirror, right=node4_mirror)
node3_mirror = TreeNode(3)
root2 = TreeNode(1, left=node3_mirror, right=node2_mirror)

# יצירת הצמתים מהתחתית כלפי מעלה
node10 = TreeNode(10)
node17 = TreeNode(17, left=node10)
node9 = TreeNode(9, right=node17)
node6_left = TreeNode(6)
node8 = TreeNode(8, left=node6_left, right=node9)
node7 = TreeNode(7, left=node8)
node12 = TreeNode(12)
node5 = TreeNode(5, left=node12, right=node7)
node6_top = TreeNode(6)
node4 = TreeNode(4, left=node6_top)
node0 = TreeNode(0)
node2 = TreeNode(2, left=node0, right=node4)
node3 = TreeNode(3, right=node5)
root_zigzag = TreeNode(1, left=node2, right=node3)




# Function 1: Inverse Tree
# Write a function `inverse_tree(root)` that receives the root of a binary tree
# and makes the tree a mirror image of itself.
# Example:
# Input Tree:
#       1
#      / \
#     2   3
#
# Output Tree:
#       1
#      / \
#     3   2


def inverse_tree(root):
    if root:
        print(root.key)
        root.left, root.right = root.right, root.left 
        inverse_tree(root.left)
        inverse_tree(root.right)




# Function 2: Boolean Mirror Trees
# Write a function `arr_mirror_trees(root1, root2)` that receives two tree roots
# and returns `True` if the trees are mirror images of each other,
# and `False` otherwise.

# Example:
# Tree 1:
#       1
#      / \
#     2   3
#
# Tree 2:
#       1
#      / \
#     3   2
# Output: True



    


# Function 3: Longest Zigzag Path
# Write a function `longest_zigzag(root)` that receives the root of a binary tree
# and returns a list of keys along the longest zigzag path.
# A "zigzag" occurs when the path alternates directions (left -> right -> left or right -> left -> right).
# The alternations do not have to be in consecutive levels of the tree to be considered part of a zigzag.
# Example:
# Tree:
#         1
#        / \
#       2   3
#      / \    \
#     0   4     5
#        /     / \
#       6     12  7
#                 /
#                8
#               / \
#              6   9
#                   \
#                   17
#                   /
#                  10

# Longest Zigzag Path: [3, 5, 7, 8, 9, 17, 10]

def longest_zigzag(root):
    i=0
    long_zigzag = []
    print(root.key) 

longest_zigzag(root_zigzag)

# Function 4: Lowest Common Ancestor
# Write a function `lowest_common_ancestor(root, node1, node2)` that receives the root of a binary tree and two nodes.
# It should return the lowest common ancestor (LCA) of the two nodes.
# Example:
# Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
#      / \
#     8   6
#        / \
#       7   10

# LCA of 8 and 10: 5
# LCA of 6 and 4: 2
# LCA of 7 and 3: 1

def lowest_common_ancestor(root, node1, node2):
    pass


# Function 5: Print Tree by Rows
# Write a function `print_tree_by_rows(root)` that prints the tree level by level using a breadth-first search (BFS).
# Example:
# Tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#
# Output:
# 1
# 2 3
# 4 5 6

def print_tree_by_rows(root):
    pass


# Instructions for Writing Tests
# Write test cases for each of the above functions. For each test:
# - Provide an example input (tree or trees for comparison).
# - Include the expected output based on the provided examples.
# - Ensure that your tests cover various edge cases, such as empty trees, single-node trees, or trees with specific structures.
# You can use helper functions to build binary trees for testing.


# Recommendation:
# To visualize binary trees, you can use the `graphviz` library. It allows you to create graphical representations of trees
# and save them as image files. This can be especially useful for debugging and understanding tree structures.
# Example:
# 1. Install Graphviz:
#    pip install graphviz
# 2. Use the following function to visualize a binary tree:

from graphviz import Digraph


def visualize_tree(root, filename="tree"):
    def add_nodes_edges(node, dot=None):
        if node:
            dot.node(str(node.key), str(node.key))
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                add_nodes_edges(node.left, dot)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                add_nodes_edges(node.right, dot)

    dot = Digraph()
    add_nodes_edges(root, dot)
    dot.render(filename, format="png", cleanup=True)  # Save as PNG
    print(f"Tree visualization saved as {filename}.png")

# This will create an image of the binary tree structure for easy reference.
