class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum_wealth = 0
        for i in range(0, len(accounts)):
            current = sum(accounts[i])
            if current > maximum_wealth:
                maximum_wealth = current
        return maximum_wealth