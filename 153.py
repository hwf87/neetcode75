# 153. Find Minimum in Rotated Sorted Array
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        TC = O(log N)
        SC = O(1)
        '''
        left, right = 0, len(nums) - 1
        res = nums[0]

        while left <= right:
            # Check if the array is rotated
            # If not, then just return the left pointer value
            # as it's been already the minumn value
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])
            # Mid is currently at the Left portion
            if nums[mid] >= nums[left]:
                left = mid + 1  
            # Mid is currently at the Right portion
            else:
                right = mid - 1
        return res

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("nums, expect", \
                             [([3,4,5,1,2], 1),
                              ([4,5,6,7,0,1,2], 0),
                              ([11,13,15,17], 11),
                              ([2], 2),
                              ([1, 2], 1),
                              ([2, 1], 1),
                              ([3,1,2], 1)]
                            )
    def test_findMin(self, nums, expect):
        '''
        '''
        answer = self.findMin(nums)
        assert answer == expect