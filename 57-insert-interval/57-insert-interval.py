class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals: return [newInterval]
        left, right = 0, len(intervals)-1
        
        best  = len(intervals)
        while left <= right:
            mid = left + (right - left)//2
            if intervals[mid][0] >= newInterval[0]:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        merged  = []
        is_meet  = False
        
        medium_interval = intervals[0] 
        if intervals[0][0] > newInterval[0]:
            medium_interval = newInterval
            is_meet = True
        elif best == len(intervals):
            intervals.append(newInterval)
            is_meet = True
        
        def merge_intervals(mediumInterval, merged):
            j = 0
            while j < len(intervals):
                nonlocal is_meet
                i  = intervals[j]
                if not is_meet and j==best:
                    is_meet  = True
                    j-=1
                    i = newInterval
                    
                if i[0] <= mediumInterval[1]:
                    mediumInterval[1] = max(i[1], mediumInterval[1])
                else:
                     merged.append(mediumInterval)
                     mediumInterval = i
                j += 1
            merged.append(mediumInterval)
            return merged
        return merge_intervals(medium_interval, [])