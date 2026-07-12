class Solution:
    def mySqrt(self, x: int) -> int: #binary search method
        if x<2:
            return x
        left=1
        right=x
        while left<=right:
            mid=(left+right)//2
            if mid**2==x:
                return mid
            elif mid**2>x:
                right=mid-1
            else:
                left=mid+1
        return right
            
