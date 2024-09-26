# https://leetcode.com/problems/my-calendar-i/description/?envType=daily-question&envId=2024-09-26
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for booking in self.calendar:
            bookingStart = booking[0]
            bookingEnd = booking[1]

            if not (start >= bookingEnd or end <= bookingStart):
                return False
        self.calendar.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
