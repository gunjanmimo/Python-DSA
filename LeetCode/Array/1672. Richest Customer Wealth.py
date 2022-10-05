class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_amount = float("-inf")
        for i in accounts:
            total_amount = sum(i)
            if total_amount>max_amount:
                max_amount = total_amount
                
        return max_amount
        