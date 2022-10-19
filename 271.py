# leetcode 271. lintcode 659. Encode and Decode Strings
class Solution:
    def encode(self, strs: list) -> str:
        '''
        TC = O(n)
        SC = O(n)
        '''
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s
        return res

    def decode(self, str: str) -> list:
        '''
        TC = O(n)
        SC = O(n)
        '''
        res, idx = [], 0
        while idx < len(str):
            idx2 = idx
            while str[idx2] != '$':
                idx2 += 1
            start = idx2 + 1
            end = start + int(str[idx:idx2])
            res.append(str[start:end])
            idx = end
        return res

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("strs, expect", \
                             [(["lint", "code", "love", "you"], "4$lint4$code4$love3$you"),
                              (["5$aa", "aa2$aa"], "4$5$aa6$aa2$aa")]
                            )
    def test_encode(self, strs, expect):
        '''
        '''
        answer = self.encode(strs)
        assert answer == expect

    @pytest.mark.parametrize("str, expect", \
                             [("4$lint4$code4$love3$you", ["lint", "code", "love", "you"]),
                              ("4$5$aa6$aa2$aa", ["5$aa", "aa2$aa"])]
                            )
    def test_decode(self, str, expect):
        '''
        '''
        answer = self.decode(str)
        assert answer == expect
    