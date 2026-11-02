# greedy? 
# Best chances are starting at the highest gas for the station?
# Best chances is starting at the start of the longest positive streak
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        current_pos_streak = 0
        current_i = 0
        best_pos_streak = 0
        best_i = 0
        for i in range(n):
            if gas[i] - cost[i] >= 0:
                current_pos_streak += gas[i] - cost[i]
            else:
                if current_pos_streak > best_pos_streak:
                    best_post_streak = current_pos_streak
                    best_i = current_i
                current_pos_streak = 0
                current_i = i + 1
        if current_pos_streak > best_pos_streak:
            best_post_streak = current_pos_streak
            best_i = current_i
        tank = 0

        for i in range(best_i, n):
            tank += gas[i]
            if tank < cost[i]:
                return -1
            else:
                tank -= cost[i]
        
        for i in range(0, best_i):
            tank += gas[i]
            if tank < cost[i]:
                return -1
            else:
                tank -= cost[i]
        
        return best_i
            

        

