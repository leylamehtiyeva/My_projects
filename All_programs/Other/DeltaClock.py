"""The DeltaClock class for calculating the time difference"""

class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2


    def __len__(self):
        diff = self.clock1.get_time() - self.clock2.get_time()
        return diff if diff>0 else 0

    def __str__(self):
        d = self.__len__()
        hour = d//3600
        minute = d % 3600 // 60
        second = d % 3600 % 60
        return f"{hour:02}: {minute:02}: {second:02}"


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if type(value) == int and value>=0:
            self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if type(value) == int and value >= 0:
            self.__minutes= value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if type(value) == int and value >= 0:
            self.__seconds = value

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds



dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)
len_dt = len(dt)
print(len_dt)

