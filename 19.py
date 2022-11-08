# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        TC = O(n)
        SC = O(1)
        '''
        # (e.g.) 
        # 1 -> 2 -> 3 -> 4 -> 5 , N = 2
        # dummy(LEFT) -> 1 -> 2 -> 3(RIGHT) -> 4 -> 5 
    
        # Create Left and Right Pointers
        # We need a Dummy node for our left pointer
        # And keep the distance between two pointers equal to N
        dummy = ListNode(val=0, next=head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1

        # keep moving right pointer till the end of list (when point to None)
        # At that moment, left pointer will point to the node
        # which is one node before the one we'd like to remove
        while right:
            left = left.next
            right = right.next
        
        # Remove the target node 
        left.next = left.next.next

        # Since we create a dummy at very begining
        # The return is going to be its next
        return dummy.next
        


