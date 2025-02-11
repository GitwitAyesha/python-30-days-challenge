# LEETCODE------->>>>> Problem:217 CONTAINS DUPLICATES
# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.
class solution:
    def containsDuplicate(self,nums:list[int]) ->bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        
sol = solution()
print(sol.containsDuplicate([1, 2, 3, 4]))  
print(sol.containsDuplicate([1, 2, 3, 1])) 
