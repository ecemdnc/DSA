class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common= strs[0]
        
        for word in strs[1:]:
            i=0
            while i<len(common) and i< len(word) and common[i]==word[i]:
                i+=1
            common= common[:i]
        
            if common== "":
                return ""
                
        return common

        