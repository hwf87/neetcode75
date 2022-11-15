# 344. Reverse String
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left <= right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp

            left += 1
            right -= 1
        return s

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("s, expect", \
                             [(["h","e","l","l","o"], ["o","l","l","e","h"]),
                              (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
                              (["A"], ["A"])]
                            )
    def test_reverseString(self, s, expect):
        '''
        '''
        answer = self.reverseString(s)
        assert answer == expect
