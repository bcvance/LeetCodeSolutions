class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        # min_costs = [0 for i in range(len(cost))]
        # for i in range(len(cost)-1, -1, -1):
        #     if i == len(cost)-1 or i == len(cost)-2:
        #         min_costs[i] = cost[i]
        #     else:
        #         cheapest = min((cost[i]+min_costs[i+1]), (cost[i]+min_costs[i+2]))
        #         min_costs[i] = cheapest
        # return min(min_costs[0], min_costs[1])


        # this solution has constant space complexity as opposed to O(n) in the solution above
        # both have O(n) time complexity
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] = min((cost[i]+cost[i+1]), (cost[i]+cost[i+2]))
        return min(cost[0], cost[1])


