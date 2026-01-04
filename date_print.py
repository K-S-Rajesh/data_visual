import time
from datetime import date,datetime,timedelta


today=date.today()
print(today.strftime("%d-%m-%y"))
from_date=today-timedelta(days=3)
to_date=today+timedelta(days=3)
print(from_date.strftime("%d-%m-%y"))
print(to_date.strftime("%d-%m-%y"))
