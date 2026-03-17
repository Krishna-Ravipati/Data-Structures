class Solution:
    def reverseWords(self, s: str) -> str:
       list(s)
       p= s.split()
       return " ".join(p[::-1])

        