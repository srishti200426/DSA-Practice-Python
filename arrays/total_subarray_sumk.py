class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        total_subarray = 0
        prefix_sum = 0

        hashmap = {0:1}

        for i in range(len(arr)):
            prefix_sum += arr[i]
            complement = prefix_sum - k

            
            

            if complement in hashmap:
                total_subarray += hashmap[complement]

            if prefix_sum in hashmap:
                hashmap[prefix_sum] += 1
            else:
                hashmap[prefix_sum] = 1


        return total_subarray
