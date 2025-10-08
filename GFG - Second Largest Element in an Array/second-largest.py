class Solution:
    def getSecondLargest(self, arr):
        
        largest = -1
        second_largest = -1
        
        for i in arr:
            
            if i > largest:
                
                second_largest= largest
                largest = i
                
            if i < largest and i > second_largest:
                
                second_largest= i
            
        if second_largest ==  -1:
            return -1
            
        else:
            return second_largest