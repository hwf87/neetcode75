# 659. Encode and Decode Strings
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here

        return ""

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

    @pytest.mark.parametrize("strs, expect", \
                             [("4$lint4$code4$love3$you", ["lint", "code", "love", "you"]),
                              ("4$5$aa6$aa2$aa", ["5$aa", "aa2$aa"])]
                            )
    def test_decode(self, strs, expect):
        '''
        '''
        answer = self.encode(strs)
        assert answer == expect
    