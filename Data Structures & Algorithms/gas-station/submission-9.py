# greedy? 
# guaranteed to be successful when total gas > total cost?
# 1 10 - 10 1 - 0 1 - 1 0
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        total_cost = 0
        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]

        if total_cost > total_gas:
            return -1
        
        tank = 0
        candidate = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                candidate = i + 1
                tank = 0
        
        return candidate
            

        

