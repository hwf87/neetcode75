# 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        '''
        hashmap = {}
        left, right, res = 0, 0, 0
        # Need to add some comment to explain in detail
        while right < len(s):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1

            while (right-left+1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
        
# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("s, k, expect", \
                             [("ABAB", 2, 4),
                              ("AABABBA", 1, 4)]
                            )
    def test_characterReplacement(self, s, k, expect):
        '''
        '''
        answer = self.characterReplacement(s, k)
        assert answer == expect