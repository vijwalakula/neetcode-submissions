# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        def dfs(node):
            if node is None:
                return
            if node.left is not None and node.right is not None:
                temp = node.left
                node.left = node.right
                node.right = temp
                dfs(node.left)
                dfs(node.right)
            elif node.left is not None and node.right is None:
                node.right = node.left
                node.left = None
                dfs(node.right)
            elif node.right is not None and node.left is None:
                node.left = node.right
                node.right = None
                dfs(node.left)

        dfs(root)
        return root
        