# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=programming-skills

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[count]
                nums[count] = temp
                count += 1
    
        return nums
        
# approach 2 4ms
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1
    
        # return nums
        
