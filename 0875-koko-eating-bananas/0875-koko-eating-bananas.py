from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def time(piles, mid):
            
            total_hrs = 0
            for i in range(0,len(piles)):
                total_hrs += ceil(piles[i]/mid)
            return total_hrs


        low = 1
        high = max(piles)

        while (low <= high):
            mid = (low + high) // 2

            time_req = time(piles,mid)

            if(time_req>h):
                low = mid + 1
            else:
                high = mid - 1

        return low 


        