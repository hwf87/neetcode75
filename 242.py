# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        TC = O(n)
        SC = O(n)
        '''       
        hashmap1 = {}
        for i in list(s):
            if i not in hashmap1:
                hashmap1[i] = 1
            else:
                hashmap1[i] += 1
                
        hashmap2 = {}
        for i in list(t):
            if i not in hashmap2:
                hashmap2[i] = 1
            else:
                hashmap2[i] += 1
        
        return hashmap1 == hashmap2
    
# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("s, t, expect", \
                             [("anagram", "nagaram", True),
                              ("rat", "car", False),
                              ("ab", "a", False),
                              ("ab", "ba", True)]
                            )
    def test_isAnagram(self, s, t, expect):
        '''
        '''
        answer = self.isAnagram(s, t)
        assert answer == expect
    