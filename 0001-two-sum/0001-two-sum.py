class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i, n in enumerate(nums):
            diff=target-n
            if diff in m:#check if needed number to satisfy the target is alr there in m
                return [m[diff],i]
            m[n]=i #store number as key and index as value
        return 