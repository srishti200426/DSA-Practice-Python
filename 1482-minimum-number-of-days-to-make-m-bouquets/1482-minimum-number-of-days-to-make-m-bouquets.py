class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(m*k > len(bloomDay)):
            return -1
        
        
        
        def possible(bloomDay,mid,m,k):
            
            b_poss = 0
            cnt = 0

            for day in bloomDay:
                if day <= mid:
                    cnt += 1
                    if cnt == k:
                        b_poss += 1
                        cnt = 0
                else:
                    cnt = 0

            return b_poss



        
        low = min(bloomDay)
        high = max(bloomDay)

        while(low<=high):
            mid = (low + high)//2
            boq_p = possible(bloomDay,mid,m,k)

            if boq_p < m:
                low = mid + 1
            else:
                
                high = mid - 1
        
        return low
        