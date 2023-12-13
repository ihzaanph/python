class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        total_seconds = self.__hour * 3600 + self.__minute * 60 + self.__second
        total_seconds += other.__hour * 3600 + other.__minute * 60 + other.__second

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return Time(hours, minutes, seconds)

    def __str__(self):
        return f"{self.__hour} hours, {self.__minute} minutes, {self.__second} seconds"

time1 = Time(1, 30, 45)
time2 = Time(2, 15, 20)

sum_time = time1 + time2
print("The sum of the times is:", sum_time)