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

# approach 2
class Solution(object):
    def findTheDifference(self, s, t):
        inventory = {}
        for char in s:
            if char in inventory:
                inventory[char] += 1
            else:
                inventory[char] = 1
        for char in t:
            if char not in inventory or inventory[char] == 0:
                return char # We found the extra letter!
            inventory[char] -= 1
