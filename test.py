import datetime

date = datetime.datetime.strptime('1/25/1968', "%m/%d/%Y")
print(type(date), date.date())