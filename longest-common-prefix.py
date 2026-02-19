#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = sorted(strs)
        first = s[0]
        last = s[-1]
        result = ""
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                result += first[i]
            else:
                break
        
        return result