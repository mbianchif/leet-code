class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        # O(n)
        chars = [x.lower() for x in s if x.isalnum()]

        i = 0
        j = len(s) - 1

        # O(n)
        while i < j:
            if chars[i] != chars[j]:
                return False

            i += 1
            j -= 1

        return True
