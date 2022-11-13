# 704. Binary Search
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        TC = O(log n)
        SC = O(1)
        '''
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("nums, target, expect", \
                             [([-1,0,3,5,9], 9, 4),
                              ([-1,0,3,5,9,12], 2, -1),
                              ([5], 5, 0),
                              ([5], 2, -1)]
                            )
    def test_search(self, nums, target, expect):
        '''
        '''
        answer = self.search(nums, target)
        assert answer == expect