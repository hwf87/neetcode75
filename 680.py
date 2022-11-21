# 680. Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        TC = O()
        SC = O()
        '''
        left, right = 0, len(s)-1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if self.validPalindrome_1(s = s[left+1:right]) == True or self.validPalindrome_1(s = s[left:right-1]) == True:
                    return True
                else: 
                    return False
        return True

    
    def validPalindrome_1(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("s, expect", \
                             [("aba", True),
                              ("abca", True),
                              ("abc", False),
                              ("a", True),
                              ("ab", True),
                              ("abab", True),
                              ("abba", True),
                              ("ececabbacec", True)]
                            )
    def test_validPalindrome(self, s, expect):
        '''
        '''
        answer = self.validPalindrome(s)
        assert answer == expect