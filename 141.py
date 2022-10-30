# 141. Linked List Cycle
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        TC = O(n)
        SC - O(n)
        '''     
        # Using hash table solution
        hashset = set()
        
        while head:
            if head in hashset:
                return True
            hashset.add(head)
            head = head.next
        return False