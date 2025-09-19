# To check for number of good pairs:
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = {}
        a = 0
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for count in freq.values():
            a += count * (count - 1) // 2
        return a
