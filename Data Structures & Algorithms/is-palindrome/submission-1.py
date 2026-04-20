class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = []
        for c in s:
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'):
                stripped.append(c.lower())
        
        return stripped == list(reversed(stripped))