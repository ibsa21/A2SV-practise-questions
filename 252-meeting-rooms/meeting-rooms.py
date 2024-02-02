class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        
        for index in range(1, len(intervals)):
            current_start, current_end = intervals[index]
            prev_start, prev_end = intervals[index-1]
            
            if current_start < prev_end:
                return False
        
        return True