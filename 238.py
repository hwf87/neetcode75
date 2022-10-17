# 238. Product of Array Except Self
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        TC = O(n)
        SC = O(n)
        '''
        answer = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer
    
# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("nums, expect", \
                             [([1,2,3,4], [24,12,8,6]),
                              ([-1,1,0,-3,3], [0,0,9,0,0])]
                            )
    def test_productExceptSelf(self, nums, expect):
        '''
        '''
        answer = self.productExceptSelf(nums)
        assert answer == expect