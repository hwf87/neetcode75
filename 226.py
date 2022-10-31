# 226. Invert Binary Tree
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        TC = O(n)
        '''
        if not root:
            return None

        # Simply switch left and right 
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Using recursive to pass through entire tree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root