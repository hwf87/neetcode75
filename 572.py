# 572. Subtree of Another Tree
# Definition for a binary tree node.
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        '''
        
        return ''
    
    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Function to check if two trees have same structure
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        Left = self.isSametree(p.left, q.left)
        Right = self.isSametree(p.right, q.right)
        isSame = Left & Right
        return isSame



        return ''

