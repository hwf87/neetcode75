# 33. Search in Rotated Sorted Array
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        TC = O(log N)
        SC = O(1)
        '''
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # When current mid is at left sorted portion
            elif nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # When current mid is at right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("nums, target, expect", \
                             [([4,5,6,7,0,1,2], 0, 4),
                              ([4,5,6,7,0,1,2], 3, -1),
                              ([1], 0, -1)]
                            )
    def test_search(self, nums, target, expect):
        '''
        '''
        answer = self.search(nums, target)
        assert answer == expect