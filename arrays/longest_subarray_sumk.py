class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        max_length = 0
        prefix_sum = 0
    
        hashmap = {0:-1}
    
        for i in range(len(arr)):
            prefix_sum = prefix_sum + arr[i]
            complement = prefix_sum - k
        
            if complement in hashmap:
                length = i - hashmap[complement]
                max_length = max(max_length,length)
            
            if prefix_sum not in hashmap:
                
                hashmap[prefix_sum] = i
            
        return max_length