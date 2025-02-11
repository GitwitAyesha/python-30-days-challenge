# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
    # or
    # s=sum(nums)
    #     n=len(nums)
    #     total=n*(n+1)//2
    #     return total-s

# Example usage:
solution = Solution()
nums = [3, 0, 1]  
print(solution.missingNumber(nums))  # Output: 2
