class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i , num in enumerate(nums):
            
            complementary = target - num

            if complementary in hashmap:
                return [hashmap[complementary],i]
            
            hashmap[num] = i 