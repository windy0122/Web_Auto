import datetime
import time

time_now = datetime.datetime.now()
time.sleep(1)
time_now1 = datetime.datetime.now()
print(time_now1-time_now)
print(str(time_now))
print(type(time_now))