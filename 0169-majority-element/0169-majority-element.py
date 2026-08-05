class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        confidence=0
        for i in nums:
            if confidence==0:
                candidate=i
            if i==candidate:
                confidence+=1
            else:
                confidence-=1
        return candidate