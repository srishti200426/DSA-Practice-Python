class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ending = nums[0]
        min_ending = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            temp_max = max_ending
            temp_min = min_ending

            max_ending = max(num,num*temp_max,num* temp_min)
            min_ending = min(num,num*temp_max,num* temp_min)

            answer = max(answer,max_ending)

        return answer
