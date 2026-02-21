class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxPft = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                pft = prices[r] - prices[l]
                maxPft = max(pft, maxPft)
            else:
                l = r
            r += 1
        return maxPft


        

    # 7 1 4 3 6 2