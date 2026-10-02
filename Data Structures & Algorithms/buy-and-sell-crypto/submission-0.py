class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while r < len(prices) and l < r:
            if(prices[l] > prices[r] and prices[r] - prices[l] < 0):
                l=r
                r=l+1
            elif(prices[r] >= prices[r]):
                if(prices[r] - prices[l] > maxP):
                    maxP = prices[r] - prices[l]
                r+=1
            

        return maxP