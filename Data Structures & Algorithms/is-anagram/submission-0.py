class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        num = sorted(s)
        num2 = sorted(t)
        if num == num2:
            return True
        return False




        