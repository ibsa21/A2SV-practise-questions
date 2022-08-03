from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
        i = bisect_left(self.calendar, [start, end])
        
        if ((i-1 >=0 and start < self.calendar[i-1][1]) or \
            (i<= len(self.calendar)-1 and end > self.calendar[i][0] )):
                return False
        
        self.calendar.insert(i, [start, end])
        return True
            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)