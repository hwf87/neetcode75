# 121. Best Time to Buy and Sell Stock
from typing import List
class Solution:
    '''
    Two Pointer solution
    '''
    def maxProfit(self, prices: List[int]) -> int:
        '''
        TC = O(n)
        SC = O(1)
        '''
        # Notice that we can always only buy left and sell on the right
        # And if we can not get any profit (Max profit <= 0) then we need to return value 0 
        left, right, max_profit= 0, 1, 0

        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                # update left pointer to a new lowest price
                left = right
            # We always update right pointer to seek a next better price
            right += 1
        return max_profit

    '''
    Below is the solution I came out
    '''    
    # def maxProfit(self, prices: List[int]) -> int:
    #     '''
    #     TC = O(n)
    #     SC = O(1)
    #     '''
    #     best_profit = 0
    #     lowest = prices[0]
    #     for price in prices:
    #         lowest = min(lowest, price)
    #         current_profit = max(0, (price - lowest))
    #         best_profit = max(best_profit, current_profit)
    #     return best_profit

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