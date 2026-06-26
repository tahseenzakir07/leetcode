class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        res=abs(x)
        rev=0
        while res>0:
            digit=res%10
            rev=rev*10+digit
            res//=10
        rev*=sign
        if rev<-2**31 or rev>2**31:
            return 0
        return rev