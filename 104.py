# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # Solution 1: DFS Recursive 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        '''
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # Solution 2: DFS

    # Solution 3: BFS