# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        TC = O(m*n)
        SC = O(n)
        '''
        hashmap = {}
        for i in strs:
            anagrams = tuple(sorted(list(i)))
            if anagrams not in hashmap:
                hashmap[anagrams] = [i]
            else:
                hashmap[anagrams] += [i]
        
        ans = list(hashmap.values())
        return ans

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("strs, expect", \
                             [(["eat","eag"], [["eat"],["eag"]]),
                              (["a"], [["a"]])]
                            )
    def test_groupAnagrams(self, strs, expect):
        '''
        '''
        answer = self.groupAnagrams(strs)
        assert answer == expect