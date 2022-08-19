class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.double_booked = []

    def book(self, start:int, end:int)->bool:
        for xstart, xend in self.double_booked:
            if start < xend and end > xstart:
                return False
        for xstart, xend in self.calendar:
            if start < xend and end > xstart:
                self.double_booked.append((max(start, xstart), min(end, xend)))
        self.calendar.append((start, end))
        return True