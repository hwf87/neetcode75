# 206. Reverse Linked List
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        TC = O(n)
        SC = O(1)
        '''

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# # Unit Test
# import pytest
# class TestCase(Solution):
#     @pytest.mark.parametrize("head, expect", \
#                              [()]
#                             )
#     def test_findMin(self, head, expect):
#         '''
#         '''
#         answer = self.findMin(head)
#         assert answer == expect