# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        TC = O(n)
        SC = O(n)
        '''
        # Stack type follow "last-in, first-out" principle
        # Which are append(), pop() operators
        stack = []

        # A hash table to link Parentheses pair
        table = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        for i in s:
            # Note we need to add condition stack != []
            # To consider the edge case like "]"
            if i in table and stack != [] and stack[-1] == table[i]:
                stack.pop()
            else:
                stack.append(i)
        return True if stack == [] else False 
        
# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("s, expect", \
                             [("()", True),
                              ("()[]{}", True),
                              ("(]", False),
                              ("[", False),
                              ("]", False)]
                            )
    def test_isValid(self, s, expect):
        '''
        '''
        answer = self.isValid(s)
        assert answer == expect
