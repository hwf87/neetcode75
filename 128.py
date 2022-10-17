# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        '''
        TC = O(n)
        SC = O(n)
        '''
        longest = 0
        numset = set(nums)
        # check whether a number is a starting number or not
        for num in nums:
            current_length = 0
            if num-1 not in numset:
                while num + current_length in numset:
                    current_length += 1
            longest = max(longest, current_length)
        return longest
    
# Method with sorted and O(nlogn)
#     def longestConsecutive(self, nums: list[int]) -> int:
#         '''
#         TC = O(N logN)
#         SC = O(n)
#         '''
#         nums = list(set(nums))
#         nums = sorted(nums, reverse = False)
        
#         if len(nums) <= 1:
#             return len(nums)

#         max_consecutive, cur_consecutive = 0, 1
#         for i in range(0, len(nums)-1):
#             if nums[i] + 1 == nums[i+1]:
#                 cur_consecutive += 1
#             else:
#                 cur_consecutive = 1
#             max_consecutive = max(max_consecutive, cur_consecutive)
#         return max_consecutive

# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("nums, expect", \
                             [([100,4,200,1,3,2], 4),
                              ([0,3,7,2,5,8,4,6,0,1], 9),
                              ([1,1,1], 1),
                              ([1], 1),
                              ([], 0)]
                            )
    def test_longestConsecutive(self, nums, expect):
        '''
        '''
        answer = self.longestConsecutive(nums)
        assert answer == expect