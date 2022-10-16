#217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        '''
        TC = O(n)
        SC = O(n)
        '''
        return len(set(nums)) != len(nums)
    
# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("test_input, expect", \
        [([1,1,2,3], True), 
         ([1,2,3,4], False),
         ([1], False)]
    )
    def test_containsDuplicate(self, test_input, expect):
        '''
        '''
        answer = self.containsDuplicate(test_input)
        assert answer == expect