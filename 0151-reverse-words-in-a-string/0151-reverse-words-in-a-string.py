class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        ans = ""
        for i in s:
            ans += i +" "
        return ans[:-1]
            