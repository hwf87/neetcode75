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
    
    # Follow up:
    # Solve this proble by SC = O(1), without a hash table 
    # Using Two pointers: Fast and Slow pointers
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        TC = O(n)
        SC - O(1)
        '''     
        slow, fast = head, head
        
        # If there's a cycle then fast and slow will finally meet each other at some moment
        # Return True 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        # Otherwise, fast pointer will finally be None to break the while loop
        # Return False
        return False