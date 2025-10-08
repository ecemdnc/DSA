class Solution:
    def reverseArray(self, arr):
        
        first_value= 0
        last_value= len(arr) -1
        
        

        while first_value < last_value:
                
            arr[first_value],arr[last_value] =arr[last_value],arr[first_value]
                
            first_value += 1
            last_value -= 1 