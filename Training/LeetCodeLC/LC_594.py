# Longest Harmonious Subsequence
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        f = {}
        l=0
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        for i in f:
            if i+1 in f:
                len = f[i+1] + f[i]
                if len > l:
                    l = len        
        return l