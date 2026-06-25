#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for i in range(n):
            if nums[i] in seen:
                return True
                break
            else:
                seen.add(nums[i])
        return False