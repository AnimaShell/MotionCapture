import datetime

t = datetime.datetime.now()
tt = str(t.year) + "_" + str(t.month) + "_" + str(t.day) + "_" + str(t.hour) + "_" + str(t.minute) + "_" + str(t.second) + "_" + str(t.microsecond)
print(tt)
