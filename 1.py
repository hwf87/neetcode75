# 1. Two Sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        TC = O()
        SC = O()
        '''
        # for i in range(0, len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums and i !=nums.index(diff):
        #         return [i, nums.index(diff)]
        
        seen = {}
        for idx in range(0, len(nums)):
            diff = target - nums[idx]
            if diff not in seen:
                seen[nums[idx]] = idx
            else:
                return [idx, seen[diff]]
            
# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("nums, target, expect", \
                              [([2,7,11,15], 9, [0,1]),
                               ([3,2,4], 6, [1,2]),
                               ([3,3], 6, [0,1])]
                             )
    def test_twoSum(self, nums, target, expect):
        '''
        '''
        answer = sorted(self.twoSum(nums, target), reverse=False)
        assert answer == expect