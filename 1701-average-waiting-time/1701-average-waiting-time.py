class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time:int = 0
        waiting_time:int = 0
        len_customer:int = 0
        for arrival, cook_time in customers:
            if arrival > current_time: current_time = arrival
            current_time += cook_time
            waiting_time += (current_time - arrival)
            len_customer +=1 
        return waiting_time/len_customer