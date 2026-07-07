
class Solution:
    def isPalindrome(self, s: str) -> bool:
        idx1 = 0
        idx2 = len(s) - 1

        while(idx1 < idx2):
            # get left ptr to alphanumeric char
            while (idx1 < idx2 and not s[idx1].isalnum()):
                idx1 += 1
            # get right ptr to alphanumeric char
            while (idx1 < idx2 and not s[idx2].isalnum()):
                idx2 -= 1
            # compare
            # mismatch
            if (s[idx1].lower() != s[idx2].lower()):
                return False
            # match
            idx1 += 1
            idx2 -= 1
        return True
