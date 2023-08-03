class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = []
        d2 = []
        for i in s:
            d1.append(s.index(i))
        for j in t:
            d2.append(t.index(j))
        return d1==d2
