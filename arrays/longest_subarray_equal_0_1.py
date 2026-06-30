class Solution:
    def maxLen(self, arr):
        # code here
        prefix_sum = 0
        max_length = 0
        
        hashmap = {0:-1}
        
        for i in range(len(arr)):
            if arr[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1
                
            if prefix_sum in hashmap:
                length = i - hashmap[prefix_sum]
                
                max_length = max(max_length,length)
                
            else:
                hashmap[prefix_sum] = i
            
        return max_length