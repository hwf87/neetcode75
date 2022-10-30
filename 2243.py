# 2423. Remove Letter To Equalize Frequency
class Solution:
    def equalFrequency(self, word: str) -> bool:
        '''
        TC = O(n)
        SC = O(n)
        '''
        hashmap = {}
        for w in word:
            hashmap[w] = hashmap.get(w, 0) + 1
            
        for k in hashmap.keys():
            hashmap[k] -= 1
            counts = hashmap.values()
            counts = [i for i in counts if i != 0]
            if len(set(counts)) == 1:
                return True
            else:
                hashmap[k] += 1
        return False

# Unit Test
import pytest 
class TestCase(Solution):
    @pytest.mark.parametrize("word, expect", \
                             [("bac", True),
                              ("abcc", True),
                              ("aabb", False),
                              ("abbcdd", False)])
    def test_equalFrequency(self, word, expect):
        '''
        '''
        answer = self.equalFrequency(word)
        assert answer == expect 