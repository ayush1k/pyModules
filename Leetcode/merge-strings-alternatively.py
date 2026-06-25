# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=programming-skills

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        lst = []
        boundary = min(len(word1), len(word2))
        for i in range(boundary):
            lst.append(word1[i])
            lst.append(word2[i])
    
        lst.append(word1[boundary : ])
        lst.append(word2[boundary : ])

        return "".join(lst)
