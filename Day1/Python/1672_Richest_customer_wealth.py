class Solution(object):
    def maximumWealth(self, accounts):
        maxwealth=0
        for customer in accounts:
            customer_wealth=sum(customer)
            maxwealth=max(customer_wealth,maxwealth)
        return maxwealth
