class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def least_days(weights,mid):
            min_days = 1
             
            total_weights = 0

            for w in weights:
                if total_weights + w > mid:

                    min_days += 1
                    total_weights = 0
                total_weights += w
            return min_days

        low = max(weights)
        high = sum(weights)

        while (low <= high):
            mid = (low + high)//2
            min_days = least_days(weights,mid)
            if(min_days > days):
                low = mid + 1
            else:
                high = mid - 1

        return low
        