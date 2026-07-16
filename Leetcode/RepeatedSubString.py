# https://leetcode.com/problems/repeated-substring-pattern/?envType=study-plan-v2&envId=programming-skills

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n =  len(s)
        for i in range(1, n//2 + 1):
            chunk = s[:i]
            multiplier = n // i
            if chunk * multiplier == s:
                return True
        return False

# approach 2
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n =  len(s)
        for i in range(1, n//2 + 1):
            if n%i == 0:
                chunks = s[: i]
                multiplier = n//i

            if (chunks * multiplier) == s:
                return True
        return False
