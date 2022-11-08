# 100. Same Tree
# Definition for a binary tree nodgite.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        TC = O(p+q)
        '''
        # Check the base case
        # if both root nodes are Null then return True
        if not p and not q:
            return True
        # if only of of root nodes is Null then retrun False
        # Note that we already check the case with both Null
        # That will not be the case hee to return False
        if not p or not q:
            return False
        # if both of roots nodes not Null but with different values then return Flase
        if p.val != q.val:
            return False
        # DFS
        Left = self.isSameTree(p.left, q.left)
        Right = self.isSameTree(p.right, q.right)
        return Left and Right

