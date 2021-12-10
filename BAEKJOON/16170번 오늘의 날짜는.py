from datetime import datetime,timedelta

a=datetime.utcnow() + timedelta(hours=9)
print(a.year)
print('%02d'%a.month)
print('%02d'%a.day)