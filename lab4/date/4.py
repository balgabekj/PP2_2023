from datetime import datetime, time

d1 = datetime.strptime('2023-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

d2 = datetime.now()

timedelta = d2 - d1

print("Seconds :",timedelta.days * 24 * 3600 + timedelta.seconds)