class Solution:
    def dectobin(self,x):
        bin=0
        i=0
        while x>0:
            r=x%2
            q=x//2
            bin=r*(10**i)+bin
            i+=1
            x=q
        return bin
    def hammingWeight(self, n: int) -> int:
        count=0
        num=self.dectobin(n)
        while num>0:
            r=num%10
            if r==1:
                count+=1
            num=num//10
        return count

        