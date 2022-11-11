# 167. Two Sum II - Input Array Is Sorted
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        TC = O(n)
        SC = O(1)
        '''
        left, right = 0, len(numbers)-1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left+1, right+1]
            elif current > target:
                right -= 1
            else:
                left += 1
                
# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("numbers, target, expect", \
                             [([2,7,11,15], 9, [1,2]),
                              ([2,3,4], 6, [1,3]),
                              ([-1,0], -1, [1,2])]
                            )
    def test_twoSum(self, numbers, target, expect):
        '''
        '''
        answer = self.twoSum(numbers, target)
        assert answer == expect