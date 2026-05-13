class Solution:
    def reverseWords(self, s: str) -> str:
        new=s.split()
        return " ".join(new[::-1])
        