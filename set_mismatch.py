class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        for i in range(len(nums)):
            if (i+1 in freq and freq[i+1] == 2 ):
                duplicate = i+1
            if i+1 not in freq:
                missing = i+1
        return[duplicate,missing]
