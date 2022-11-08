# 143. Reorder List
# Definition for singly-linked list.
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        TC = O(n)
        SC = O(n)
        """
        
        # Using Slow and Fast Pointer to divide list into 2 portion
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # The Second portion Head is the next of the First portion tail
        second = slow.next
        
        # Make sure first portion point to None at the end 
        slow.next = None
        
        # Reverse second portion
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Merge First and Second portion
        # The Second length will equal or lower than length of First portion 
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2