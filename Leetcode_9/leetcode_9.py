class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = list(str(x))
        for i in l:
            if i!=l.pop():
                return False
        return True