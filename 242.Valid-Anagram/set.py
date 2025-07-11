class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # O(n)
        S = {x: s.count(x) for x in set(s)}

        # O(n)
        T = {x: t.count(x) for x in set(t)}
        return S == T
