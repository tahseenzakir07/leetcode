class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
        ans=sorted(freq, key=freq.get, reverse=True) #freq.get gets the value of they key and reverse=true implies decending order
        return ans[:k]