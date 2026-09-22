# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = [1]

        def dfs(node, curr_l):
            if node is None:
                return
            if node.left is not None:
                depth[0] = max(depth[0], curr_l +1)
                dfs(node.left, curr_l+1)
            if node.right is not None:
                depth[0] = max(depth[0], curr_l+1)
                dfs(node.right, curr_l+1)
        dfs(root, 1)
        return depth[0]


        