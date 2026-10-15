class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicti = {}

        for a in s:
            dicti[a] = dicti.get(a, 0) + 1
        for b in t:
            if dicti.get(b, 0) == 0:
                return False
            dicti[b] -= 1
        return True

        