# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/?envType=study-plan-v2&envId=programming-skills
# approach 1
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        for i in nums:
            product *= i
    
        if product == 0:
            return 0
        elif product > 0:
            return 1
        else:
            return -1

# approach 2
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sign = 1
        for i in nums:
            if i == 0:
                return 0
            if 0 > i:
                sign = - sign

        return sign
