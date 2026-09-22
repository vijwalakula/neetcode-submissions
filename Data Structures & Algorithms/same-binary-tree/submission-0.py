# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = collections.deque([(p, q)])

        while que:
            nums = len(que)
            for _ in range(nums):
                (node1, node2) = que.popleft()
                if node1 is None and node2 is None:
                    continue
                if (node1 is not None and node2 is None) or (node1 is None and node2 is not None):
                    return False
                if node1.val != node2.val:
                    return False
                que.append((node1.left, node2.left))
                que.append((node1.right, node2.right))
        return True
            
        