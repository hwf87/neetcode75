# 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        TC = O(n)
        SP = O(n)
        '''
        left, right, longest = 0, 0, 0
        table = {}
        
        while right < len(s):            
            # update hash table while increasing right pointer every time
            table[s[right]] = table.get(s[right], 0) + 1
            
            # Non-Valid result => Not enough K to replace current window to be unique 
            # Window size - value of character most count > K character can be replaced 
            
            while (right - left + 1) - max(table.values()) > k:
                # If reslut is NOT valid:
                # Keep update hash table and adding left pointer by 1
                # Until the result is valid 
                table[s[left]] -= 1
                left += 1
                
            # Calculate longest result
            # Note the result need to be calculated before right pointer is updated
            longest = max(longest, right - left + 1)
            
            # If reslut is valid: 
            # Increase right pointer by 1
            right += 1   
        return longest

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