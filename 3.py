# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        TC = O(n)
        SP = O(n)
        '''
        left, right, longest = 0, 0, 0

        charset = set()
        while right < len(s):
            while s[right] in charset:
                # Once we found the next character will raise duplicate, we will directly remove the character on the left 
                # However, that character might not the one which is raising duplicte
                # We will keep removing left words using [left + 1]
                # Until we removes the duplicate character, which is = "s[right]"
                charset.remove(s[left])
                left += 1
            
            # Add the new character to the set then Calculate the result
            charset.add(s[right])
            current_length = right - left + 1
            longest = max(longest, current_length)

            # Keep moving right pointer until the end
            right += 1
        return longest
    
# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("s, expect", \
                             [("abcabcbb", 3),
                              ("bbbbb", 1),
                              ("pwwkew", 3)]
                            )
    def test_lengthOfLongestSubstring(self, s, expect):
        '''
        '''
        answer = self.lengthOfLongestSubstring(s)
        assert answer == expect