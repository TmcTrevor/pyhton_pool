import datetime
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
date3 = datetime.date(2020,9,7)
dayAfter = date3 + delta



# date = datetime.datetime.now()
# date2 = datetime.datetime(2020,9,7)



print(dayAfter)
# print(date3)
# print(datetime.date.year)
# print(date.month, date.day, date.year)