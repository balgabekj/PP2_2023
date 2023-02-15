import datetime

today=datetime.date.today()
x=datetime.timedelta(1)
yesterday=today-x
tommorow=today+x

print("Current date:", today)
print("tommorow date:", tommorow)
print("yesterday date:", yesterday)