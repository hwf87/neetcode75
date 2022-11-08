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
        TC = O(n*m)
        '''
        # Consider Edge case
        # if subRoot is Null, then itself can be a sub of any root
        if not subRoot:
            return True
        # If subRoot is not Null, but Root is Null, then return False.
        # Noted we pass the pervious codiction, means subRoot must not be Null here
        if not root:
            return False
        # After making sure both of them are not Null
        # We can compare if they are the same tree
        if self.isSametree(root, subRoot):
            return True
        # If not they are not same, keep comparing recursively till the end
        return (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )
    
    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Leetcode 100.
        Function to check if two trees have same structure
        '''
        # Consider Edge case
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return (
            self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)
        )