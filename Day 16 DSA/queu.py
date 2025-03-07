#leetcode problem number 215
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]        
sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(sol.findKthLargest(nums, k))