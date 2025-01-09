class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, left=node4, right=node5)
node3 = TreeNode(3)
root1 = TreeNode(1, left=node2, right=node3)

node4_mirror = TreeNode(4)
node5_mirror = TreeNode(5)
node2_mirror = TreeNode(2, left=node5_mirror, right=node4_mirror)
node3_mirror = TreeNode(3)
root2 = TreeNode(1, left=node3_mirror, right=node2_mirror)

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


#a print a tree
# def print_tree(root):
#     if root:
#         print (root.key)
#         print_tree(root.left)
#         print_tree(root.right)
# print_tree(root_zigzag)


#b print a tree with side expression
# def print_tree(root, direction = None):
#     if root is None:
#         return
#     if not direction:
#         print (root.key)
#     else:
#         print(root.key, "=>", direction)
#     print_tree(root.left, "left")
#     print_tree(root.right, "right")
# print_tree(root_zigzag)

#c find one zigzag path
# counter = 0
# path = []
# def print_tree(node, prev_direction = None, current_length=0):
#     if node is None:
#         return current_length
#     elif node.



def longest_zigzag_path(node, prev_direction=None, current_length=0):
    if node is None:
        return current_length
    
    print(f"Visiting Node: {node.key}, Prev Direction: {prev_direction}, Current Length: {current_length}")

    if prev_direction != "left":
        left_zigzag = longest_zigzag_path(node.left, "left", current_length + 1)
    else:
        left_zigzag = longest_zigzag_path(node.left, "left", 1)

    if prev_direction != "right":
        right_zigzag = longest_zigzag_path(node.right, "right", current_length + 1)
    else:
        right_zigzag = longest_zigzag_path(node.right, "right", 1)

    return max(left_zigzag, right_zigzag, current_length)


result = longest_zigzag_path(root_zigzag)
print("Longest Zigzag Path Length:", result)

#1
# def inverse_tree(root):
#     if root:
#         print(root.key)
#         root.left, root.right = root.right, root.left 
#         inverse_tree(root.left)
#         inverse_tree(root.right)


#3
# def arr_mirror_trees(root1, root2):
#     if not root1 or not root2:
#         return root1 == root2
#     elif root1.key != root2.key: return False
#     else: 
#         return (arr_mirror_trees(root1.left, root2.right)
#         and arr_mirror_trees(root1.right, root2.left))
    
        
# long_zigzag = []
# changes = []
# counter = 0
# i=0
# def longest_zigzag(root):
#     root(self, key, direction, left=None, right=None)
#         return long_zigzag
#     else:
#         long_zigzag.append(root.key)
#         if root.left:
#             changes.append(1)
#             longest_zigzag(root.left)
#         elif root.right:
#             changes.append(2)
#             longest_zigzag(root.right)
#         return long_zigzag, changes

# print(longest_zigzag(root_zigzag))
    
  
   
        
