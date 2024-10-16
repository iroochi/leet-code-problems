class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        if new_s == new_s[::-1]:
            return True
        else:
            return False    