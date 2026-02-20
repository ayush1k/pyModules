#https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        inventory = {}
        for i in magazine:
            if i in inventory:
                inventory[i] += 1
            else:
                inventory[i] = 1
        
        for i in ransomNote:
            if i not in inventory or inventory[i] == 0:
                return False
            inventory[i] -= 1
        
        return True