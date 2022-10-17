# 11. Container With Most Water
class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        TC = O(n)
        SC = O(1)
        '''
        answer, left, right = 0, 0, len(height) - 1
        while right > left:
            area = (right - left) * min(height[left], height[right])
            answer = max(area, answer)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1     
        return answer

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("height, expect", \
                             [([1,8,6,2,5,4,8,3,7], 49),
                              ([1,1], 1)]
                             )
    def test_maxArea(self, height, expect):
        '''
        '''
        answer = self.maxArea(height)
        assert answer == expect