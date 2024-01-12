import datetime

# 현재 날짜
now = datetime.date.today()
print(now)

now = datetime.datetime.today()
print(now)

print(now.year)
print(now.month)
print(now.day)

# 지정된 날짜
date = datetime.datetime(2024,1,1,12,0,0)
print(date)
