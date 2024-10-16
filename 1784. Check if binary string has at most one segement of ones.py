class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s = s.rstrip("0")
        if "0" in s:
            return False
        return True