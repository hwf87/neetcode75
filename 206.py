# 206. Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = ListNode(val)
        # if head is None, which means the first Node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

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

def create_my_linked_list(mylist: list) -> SingleLinkedList:
    '''
    mylist = [1, 2, 3, 4, 5]
    '''
    MyLinkedList = SingleLinkedList()
    for node in mylist:
        MyLinkedList.append(node)
    return MyLinkedList


a = create_my_linked_list([1,2,3]).head
print(a)
print(a.val)


# print(SL)
# print(type(SL))
# print(SL.head)
# print(SL.head.val)
# print(SL.head.next)
# print(SL.head.next.val)
# print(SL.head.next.next.val)
# print(SL.head.next.next.next.val)
# print(SL.head.next.next.next.next.val)

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("head, expect", \
                             [([1,2,3,4,5], [5,4,3,2,1])]
                            )
    def test_reverseList(self, head, expect):
        '''
        '''
        head = create_my_linked_list(head).head
        expect = create_my_linked_list(expect).head

        answer = self.reverseList(head)
        assert answer == expect