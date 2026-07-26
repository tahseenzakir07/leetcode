class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        twice={}
        for i in nums:
            if i not in twice:
                twice[i]=1
            elif i in twice:
                return True
        return False