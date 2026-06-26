class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        num=0
        for i in digits:
            num=num*10 + i
        last=digits[n-1]
        if last<9:
            digits[n-1]+=1
            return digits
        else:
            num+=1
            if digits[0]!=9:
                new=[0]*n
                i=n-1
            else:
                new=[0]*(n+1)
                i=n
            while i>=0:
                d=num%10
                new[i]=d
                num=num//10
                i-=1
            if new[0]==0:
                new.remove(0)
            return new