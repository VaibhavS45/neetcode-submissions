class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini,profit=prices[0],0
        for i in range(len(prices)):
            sell=prices[i]-mini
            profit=max(profit,sell)
            mini=min(prices[i],mini)
        return profit    