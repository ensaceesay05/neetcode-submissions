class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        best = 0

        for r in range (len(prices)):
            if prices [l] < prices[r]:
                best = max(best, prices [r] - prices[l])
            if prices[l] >= prices[r]:
                l = r

        return best