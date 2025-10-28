class Solution:
	def pushZerosToEnd(self, arr):
    	
        point= 0
        for i in range(len(arr)):
            
            if arr[i]!= 0:
                
                arr[i],arr[point]= arr[point],arr[i]
                
                point +=1