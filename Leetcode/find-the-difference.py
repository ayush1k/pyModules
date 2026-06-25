# https://leetcode.com/problems/find-the-difference/?envType=study-plan-v2&envId=programming-skills

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        new1 = sorted(s)
        new2 = sorted(t)
        for i in range(len(s)):
            if new1[i] != new2[i]:
                return new2[i]
        return new2[-1]
