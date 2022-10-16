# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        TC = O(n)
        SC = O(n)
        '''
        s = s.lower()
        s = [letter for letter in s if letter.isalnum()]
        left, right = 0, len(s)-1
        
        while left <= right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

# unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("s, expect", \
                             [("A man, a plan, a canal: Panama", True),
                              ("race a car", False),
                              (" ", True)]
                            )
    def test_isPalindrome(self, s, expect):
        '''
        '''
        answer = self.isPalindrome(s)
        assert answer == expect