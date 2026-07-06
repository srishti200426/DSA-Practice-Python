class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_max = 0
        count = 0

        for i in range(len(nums)):
            
            if nums[i] == 1:
                
                count += 1
                count_max = max(count_max,count)

            else:
                count = 0

        return count_max
        