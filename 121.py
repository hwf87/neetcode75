# 121. Best Time to Buy and Sell Stock
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        TC = O(n)
        SC = O(1)
        '''
        best_profit = 0
        lowest = prices[0]
        for price in prices:
            lowest = min(lowest, price)
            current_profit = max(0, (price - lowest))
            best_profit = max(best_profit, current_profit)
        return best_profit

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("prices, expect", \
                             [([7,1,5,3,6,4], 5),
                              ([7,6,4,3,1], 0)]
                             )
    def test_maxProfit(self, prices, expect):
        '''
        '''
        answer = self.maxProfit(prices)
        assert answer == expect