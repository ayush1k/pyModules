# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=programming-skills

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        window_size = len(needle)
        boundary = (len(haystack) - window_size) + 1
        for i in range(boundary):

            current_window = haystack[i : i + window_size]

            if current_window == needle:
                return i
        return - 1
