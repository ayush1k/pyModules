# https://leetcode.com/problems/plus-one/
# approach 1
class Solution(object):
    def plusOne(self, digits):
        temp = int("".join(map(str, digits)))
        temp += 1
        temp = str(temp)
        L =[]
        for i in range(len(temp)):
            L.append(int(temp[i]))
        return L
# approach 2

class Solution(object):
    def plusOne(self, digits):
        # Your exact math logic
        temp = int("".join(map(str, digits)))
        temp += 1
        
        # The Pythonic way to turn a string back into an integer array!
        return [int(x) for x in str(temp)]
