class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        intuition:
        1. iterate the array once, considering the value at either buying (min) or selling (max). The pair might get better or worse
        """
        best_buy_price = sys.maxsize  # Integer.max
        max_profit = 0

        for price in prices:
            # what if we sell here?
            max_profit = max(max_profit, price - best_buy_price)

            # should we buy here?
            best_buy_price = min(price, best_buy_price)
        
        return max_profit