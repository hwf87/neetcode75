# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        '''
        TC = O(n)
        SC = O(n)
        '''
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        print(hashmap)
        hashmap = {k:v for k,v in sorted(hashmap.items(), key=lambda item : item[1], reverse=True)}

        print(hashmap)
        ans =  list(hashmap.keys())[:k]
        return ans


# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("nums, k, expect", \
                             [([1,1,1,2,2,3], 2, [1,2]),
                              ([1], 1, [1])]
                            )
    def test_topKFrequent(self, nums, k, expect):
        '''
        '''
        answer = self.topKFrequent(nums, k)
        assert answer == expect