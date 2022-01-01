class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda a:a[0])
        mediumInterval  = intervals[0]
        print(mediumInterval)
        merged = []
        for i in intervals:
            if i[0] <= mediumInterval[1]:
                mediumInterval[1] = max(i[1], mediumInterval[1])
            else:
                 merged.append(mediumInterval)
                 mediumInterval = i
        merged.append(mediumInterval)
        return merged
            
