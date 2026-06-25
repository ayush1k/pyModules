#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chrs = []
        for i in s:
            if i.isalnum():
                cleaned_chrs.append(i.lower())
        
        cleaned = ''.join(cleaned_chrs)
        
        return cleaned == cleaned[::-1]