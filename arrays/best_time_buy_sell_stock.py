class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        i = 0
        j = 1

        while(j < len(prices)):
            if(prices[j] - prices[i]< 0):
                i = j

            else:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit,profit)
                j+=1

        return max_profit