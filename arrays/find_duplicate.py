class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        
        #finding the point where tortoise and hare meets
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast :
                break

        
        #finding duplicate number
        slow = nums[0]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]

        return slow