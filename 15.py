# 15. 3Sum
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        TC = O(n^2)
        SC = O(1)
        '''
        res = []
        # Sorting a list is costing O(N logN)
        nums.sort() 
        # Two loops are costing O(n^2)
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx-1]:
                continue
            left, right = idx+1, len(nums) - 1
            while left < right:
                if nums[idx] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[idx] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([nums[idx], nums[left], nums[right]])
                    # Here we still need to update either one of left or right pointer
                    # Otherwise the while loop will never end
                    left += 1

                    # However, it's possible that the the numbers are the same [left = left + 1]
                    # We're going to keep increasing left until we meet a different number
                    # Or until left has already larger than right
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("nums, expect", \
                             [([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
                              ([0,1,1], [])]
                            )
    def test_threeSum(self, nums, expect):
        '''
        '''
        answer = self.threeSum(nums)
        assert answer == expect