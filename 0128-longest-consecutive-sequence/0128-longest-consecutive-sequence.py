class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsets=set(nums)
        longest=0
        for i in numsets:
            if i-1 not in numsets:
                length=1
                while i+length in numsets:
                    length+=1
                longest=max(longest, length)
        return longest