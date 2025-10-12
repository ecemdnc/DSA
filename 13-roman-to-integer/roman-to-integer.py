class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }  

        reverse_s= s[::-1]

        total= roman_numbers[reverse_s[0]]
        prev_val= roman_numbers[reverse_s[0]]
        
        for i in reverse_s[1:]:
            if prev_val> roman_numbers[i]:
                total-=roman_numbers[i]
            else:
                total+= roman_numbers[i]

            prev_val= roman_numbers[i]
            
        return total

