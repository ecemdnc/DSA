class Solution:
    def isValid(self, s: str) -> bool:
        
        open_brackets= []
        dictionary= {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i== "(" or i== "[" or i== "{" :
                open_brackets.append(i)

            elif i in dictionary:

                if not open_brackets:
                    return False

                if open_brackets[-1] == dictionary[i]:
                    open_brackets.pop()
            
                else:
                    return False
        
        return not open_brackets