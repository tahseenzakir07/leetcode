class Solution:
    def addDigits(self, num: int) -> int:
        #usual approach- O(n)
        while num>=10:
            num=sum(int(d) for d in str(num))
        return num
