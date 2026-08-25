class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for i in s:
            if i.isalnum():
                new+=i
        new=new.lower()
        start=0
        end=(len(new)-1)
        while start<=end:
            if new[start]!=new[end]:
                return False
            start+=1
            end-=1
        return True