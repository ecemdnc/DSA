class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        string_x = str(x)
        reverse_str= string_x[::-1]
        reverse_x = int(reverse_str)

        if x == reverse_x:
            return True
        else:   
            return False